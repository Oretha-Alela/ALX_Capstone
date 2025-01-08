from django.test import TestCase
from .models import InventoryItem, User

class InventoryItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="testuser@example.com", password="testpass")
        self.item = InventoryItem.objects.create(
            name="Test Item",
            description="Test Description",
            quantity=10,
            price=100.0,
            category="Test Category",
            user=self.user,
        )

    def test_inventory_item_creation(self):
        self.assertEqual(self.item.name, "Test Item")
        self.assertEqual(self.item.quantity, 10)






from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, InventoryItem

class InventoryAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

    def test_create_inventory_item(self):
        data = {
            "name": "Test Item",
            "description": "Test Description",
            "quantity": 10,
            "price": 50.0,
            "category": "Test Category"
        }
        response = self.client.post("/inventory/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InventoryItem.objects.count(), 1)
