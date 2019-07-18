from django.urls import path

from .views import BankDetailAPIView, BranSearchAPIView

app_name = 'branches'

urlpatterns = [
    path('', BranSearchAPIView.as_view(), name='ifsc_search'),
    path('branch/', BankDetailAPIView.as_view(), name='info'),
]
