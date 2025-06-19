from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='lawyer-register'),
    path('login/', LoginView.as_view(), name='lawyer-login'),
    path('logout/', LogoutView.as_view(), name='lawyer-logout'),
    path('profile/', ProfileView.as_view(), name='lawyer-profile'),
]
