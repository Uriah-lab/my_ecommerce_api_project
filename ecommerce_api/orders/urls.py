from django.urls import path
from .views import OrderListCreateView

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list-create'),  # Ensure this route is correct
]
