from django.urls import path
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken

from .views import RegisterAPIView


app_name = 'users'


urlpatterns = [
    path('signup/', RegisterAPIView.as_view(), name='register'),
    path('api-token-auth/', ObtainJSONWebToken.as_view(), name='login'),
    path('api-token-refresh/', RefreshJSONWebToken.as_view(), name='refresh_token'),
    path('api-token-verify/', VerifyJSONWebToken.as_view(), name='verify_token'),

]
