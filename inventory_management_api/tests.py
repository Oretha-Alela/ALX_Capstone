from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import InventoryItem

class InventoryAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")

    def test_create_inventory_item(self):
        data = {"name": "Test Item", "quantity": 10, "price": 100.0}
        response = self.client.post("/api/inventory/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class InventoryAPITestCase(APITestCase):
    def setUp(self):
        InventoryItem.objects.create(name="Item1", quantity=10, price=100, category="Electronics")
        InventoryItem.objects.create(name="Item2", quantity=3, price=50, category="Groceries")

    def test_get_inventory_items(self):
        response = self.client.get('/inventory/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_filter_low_stock(self):
        response = self.client.get('/inventory/?low_stock=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)  



from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import InventoryItem, InventoryChangeLog

class InventoryChangeLogTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.item = InventoryItem.objects.create(name="Test Item", quantity=10, price=100.0, category="Test Category")

    def test_log_inventory_change(self):
        self.item.quantity = 15
        self.item.save()

        
        logs = InventoryChangeLog.objects.filter(item=self.item)
        self.assertEqual(logs.count(), 1)
        log = logs.first()
        self.assertEqual(log.quantity_before, 10)
        self.assertEqual(log.quantity_after, 15)

    def test_get_change_logs(self):
        InventoryChangeLog.objects.create(item=self.item, user=self.user, quantity_before=10, quantity_after=15)
        response = self.client.get(f'/inventory/{self.item.id}/logs/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

