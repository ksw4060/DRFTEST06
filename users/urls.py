from django.urls import path
from users.views import CustomTokenObtainPairView
from users import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='sign_up_view'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='login_view'),
    path('<int:id>/', views.UserView.as_view(), name='user_view')

]
