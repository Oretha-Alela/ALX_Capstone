
from rest_framework import serializers
from .models import InventoryItem

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'

    def validate(self, data):
        if data['quantity'] < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        if data['price'] < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return data
