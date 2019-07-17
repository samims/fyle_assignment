from django.urls import path
from .views import BankListAPIView, BankDetailAPIView, BranSearchAPIView
urlpatterns = [
    # path('', BankListAPIView.as_view()),
    path('', BranSearchAPIView.as_view()),
    path('branch/', BankDetailAPIView.as_view()),
]
