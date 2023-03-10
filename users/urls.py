from django.urls import path
from .views import RegisterView, LoginView, AuthenticatedUser, LogoutView
urlpatterns = [
    path("register", RegisterView.as_view()),
    path("login", LoginView.as_view()),
    path("authenticateUser", AuthenticatedUser.as_view()),
    path("logout", LogoutView.as_view())
]
