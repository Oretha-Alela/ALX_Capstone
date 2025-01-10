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
