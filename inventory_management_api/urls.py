"""
from django.urls import path
# from .views import InventoryView
from django.contrib.auth import views as auth_views
from .views import InventoryItemListCreateView, InventoryItemDetailView, InventoryChangeLogView, InventoryItemListView

urlpatterns = [
    path('inventory/', InventoryItemListCreateView.as_view(), name='inventory-list-create'),
    path('inventory/<int:pk>/', InventoryItemDetailView.as_view(), name='inventory-detail'),
    path('inventory/<int:item_id>/logs/', InventoryChangeLogView.as_view(), name='inventory-change-logs'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('inventory/', InventoryView.as_view(), name='inventory'),
    path('inventory/', InventoryItemListView.as_view(), name='inventory-list'),
]
"""




from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    InventoryItemListCreateView,
    InventoryItemDetailView,
    InventoryChangeLogView,
    InventoryItemListView
)

urlpatterns = [
    path('inventory/', InventoryItemListCreateView.as_view(), name='inventory-list-create'),
    path('inventory/<int:pk>/', InventoryItemDetailView.as_view(), name='inventory-detail'),
    path('inventory/<int:item_id>/logs/', InventoryChangeLogView.as_view(), name='inventory-change-logs'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('inventory/', InventoryItemListView.as_view(), name='inventory-list'),
]
















