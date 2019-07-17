from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Q
from .models import Branches
from .serializers import BranchSerializers


class BankListAPIView(generics.ListAPIView):
    serializer_class = BranchSerializers
    queryset = Branches.objects.all()[:200]
    permission_classes = (AllowAny,)


class BankDetailAPIView(generics.RetrieveAPIView):
    serializer_class = BranchSerializers
    queryset = Branches.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        ifsc = self.request.query_params.get("ifsc")
        obj = get_object_or_404(queryset, pk=ifsc)
        return obj


class BranSearchAPIView(generics.ListAPIView):
    """
    View for getting Branchlist
    """

    serializer_class = BranchSerializers
    queryset = Branches.objects.select_related("bank").all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        queryset filtering by queryparams
        """
        bank_name = self.request.query_params.get("name")
        city = self.request.query_params.get("city")
        qs = self.queryset
        if bank_name:
            qs = self.queryset.filter(bank__name__icontains=bank_name)
        if city:
            qs = qs.filter(city__icontains=city)
        return qs
