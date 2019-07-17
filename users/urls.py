from django.urls import path
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken

from .views import RegisterAPIView

urlpatterns = [
    path('signup/', RegisterAPIView.as_view()),
    path('api-token-auth/', ObtainJSONWebToken.as_view()),
    path('api-token-refresh/', RefreshJSONWebToken.as_view()),
    path('api-token-verify/', VerifyJSONWebToken.as_view()),

]
