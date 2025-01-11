from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import InventoryItem, InventoryChangeLog
from .serializers import InventoryItemSerializer, InventoryChangeLogSerializer

class InventoryItemListCreateView(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class InventoryItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class InventoryChangeLogView(generics.ListAPIView):
    
    class InventoryChangeLogView(generics.ListAPIView):
        serializer_class = InventoryChangeLogSerializer

    def get_queryset(self):
        item_id = self.kwargs['item_id']
        return InventoryChangeLog.objects.filter(item_id=item_id).order_by('-change_time')








from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inventory-list')  # Replace with your inventory URL name
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout


    

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import InventoryItem
from .serializers import InventoryItemSerializer

class InventoryItemListCreateView(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        return JsonResponse({"message": "Authenticated access"})


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import InventoryItem

class InventoryListView(LoginRequiredMixin, ListView):
    model = InventoryItem
    template_name = "inventory_list.html"






from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from .models import InventoryItem
from .serializers import InventoryItemSerializer

class InventoryItemListCreateView(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    filterset_fields = ['category', 'price']
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['price', 'quantity', 'name', 'date_added']  # Allows sorting
    pagination_class = PageNumberPagination


class InventoryItemListView(generics.ListAPIView):
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        low_stock_threshold = self.request.query_params.get('low_stock', None)
        if low_stock_threshold:
            queryset = queryset.filter(quantity__lt=int(low_stock_threshold))
        
        # Price range filter
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        
        return queryset









from .permissions import IsOwnerOrReadOnly

class InventoryItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
