from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from .models import InventoryItem, InventoryChangeLog
from .serializers import InventoryItemSerializer, InventoryChangeLogSerializer
from .permissions import IsOwnerPermission
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



# List and Create Inventory Items
class InventoryItemListCreateView(generics.ListCreateAPIView):
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category', 'price']
    ordering_fields = ['name', 'quantity', 'price', 'date_added']

    def get_queryset(self):
        return InventoryItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Retrieve, Update, and Delete Inventory Items
class InventoryItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

# Inventory Change History
class InventoryChangeLogView(generics.ListAPIView):
    serializer_class = InventoryChangeLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        item_id = self.kwargs.get('item_id')
        return InventoryChangeLog.objects.filter(item_id=item_id)

class CustomTokenObtainView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
  
        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # Generate tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)