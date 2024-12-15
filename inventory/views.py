from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Item
from .serializers import ItemSerializer

class ListItemsView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CreateItemView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
