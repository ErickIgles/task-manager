from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api.views import UserCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('detail/user/', UserRetrieveUpdateDestroyView.as_view(), name='detail-user'),
]
