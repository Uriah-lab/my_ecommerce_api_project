from django.urls import path
from .views import CartListCreateView, CartDetailView

urlpatterns = [
    path('', CartListCreateView.as_view(), name='cart-list-create'),  # POST, GET
    path('<int:pk>/', CartDetailView.as_view(), name='cart-detail'),  # PUT, DELETE
]
