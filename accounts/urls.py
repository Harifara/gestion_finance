from django.urls import path
from .views import RegisterView, profile_view, AdminOnlyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', profile_view, name='profile'),
    path('adminonly/', AdminOnlyView.as_view(), name='admin_only'),
]



urlpatterns += [
    path('logout/', LogoutView.as_view(), name='logout'),
]