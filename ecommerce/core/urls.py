from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home.core"),
    path('view/<slug>/', views.ListViewCategory.as_view(), name="category.core"),
]