from django.urls import path
from .views import payment_form, card_details

urlpatterns = [
    path('payment_details/<int:pk>/', payment_form, name="user.details"),
    path('card_details/', card_details, name="user.card")
]