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
    serializer_class = InventoryChangeLogSerializer

    def get_queryset(self):
        return InventoryChangeLog.objects.filter(item_id=self.kwargs['item_id'])


from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login successful"})
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=401)


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return JsonResponse({"message": "Logout successful"})



from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class InventoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Authenticated access"})


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class InventoryView(LoginRequiredMixin, TemplateView):
    template_name = "inventory.html"





from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination

class InventoryItemListCreateView(generics.ListCreateAPIView):
    ...
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category', 'price']
    ordering_fields = ['name', 'quantity', 'price', 'date_added']
    pagination_class = PageNumberPagination
