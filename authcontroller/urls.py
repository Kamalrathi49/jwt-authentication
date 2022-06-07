from django.conf.urls import url
from django.urls import path, include
from authcontroller.api import RegisterApi
from rest_framework_simplejwt import views as jwt_views
from authcontroller.views import MyTokenObtainPairView


urlpatterns = [
    path('api/register', RegisterApi.as_view()),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]