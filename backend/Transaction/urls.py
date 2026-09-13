from django.urls import path
from .views import TransactionViewSet

urlpatterns = [
    path('transaction/', TransactionViewSet),
]