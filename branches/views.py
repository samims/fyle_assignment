from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Branches
from .serializers import BranchSerializers


class BankDetailAPIView(generics.ListAPIView):
    """
    API for Find Branch by IFSC code
    """

    serializer_class = BranchSerializers
    queryset = Branches.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """

        :return: query after filtering by ifsc list
        """
        queryset = self.queryset
        ifsc = self.request.query_params.get("ifsc")
        if ifsc:
            # supporting multiple param value
            ifsc_list = ifsc.split(",")
            queryset = self.queryset.filter(ifsc__in=ifsc_list)
        return queryset


class BranchSearchAPIView(generics.ListAPIView):
    """
    View for getting Branchlist
    """

    serializer_class = BranchSerializers
    queryset = Branches.objects.select_related("bank").all().order_by("bank")
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        queryset filtering by queryparams
        """
        bank_name = self.request.query_params.get("name")
        city = self.request.query_params.get("city")
        qs = self.queryset
        if bank_name:
            qs = qs.filter(bank__name__icontains=bank_name)
        if city:
            qs = qs.filter(city__icontains=city)
        return qs
