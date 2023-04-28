from django.urls import path, include
from users.views import CustomTokenObtainPairView
from users.views import UserView, ProfileView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('signup', UserView.as_view(), name='user_view'),
    path('profile/<int:user_id>', ProfileView.as_view(), name='profile_view'),
    path('api/token/', CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
