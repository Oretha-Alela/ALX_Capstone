from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)





class InventoryChangeLog(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name="change_logs")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    quantity_before = models.PositiveIntegerField()
    quantity_after = models.PositiveIntegerField()
    change_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Change for {self.item.name} by {self.user.username if self.user else 'Unknown'}"