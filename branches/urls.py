from django.urls import path

from .views import BankDetailAPIView, BranchSearchAPIView

app_name = 'branches'

urlpatterns = [
    path('', BankDetailAPIView.as_view(), name='ifsc_search'),
    path('branch/', BranchSearchAPIView.as_view(), name='info'),
]
