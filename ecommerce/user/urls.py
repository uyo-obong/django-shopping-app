from django.urls import path
from .views import register_user, login_user, user_logout, contact_us

urlpatterns = [
    path('contact_us/', contact_us, name="contact.user"),
    path('register/', register_user, name="register.user"),
    path('accounts/login/', login_user, name="login.user"),
    path('logout/', user_logout, name="logout.user")
]