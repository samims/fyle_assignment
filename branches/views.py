import operator
from functools import reduce

from django.db.models import Q
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


class BranSearchAPIView(generics.ListAPIView):
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
        bank_names = self.request.query_params.get("name")
        cities = self.request.query_params.get("city")
        qs = self.queryset
        query = None
        if bank_names:
            bank_names = bank_names.split(",")
            query = reduce(
                operator.or_,
                (Q(bank__name__icontains=bank_name) for bank_name in bank_names),
            )
            qs = qs.filter(query)
        if cities:
            cities = cities.split(",")
            # query for city and name both
            query = reduce(
                operator.and_,
                (
                    Q(query),
                    Q(
                        reduce(
                            operator.or_, (Q(city__icontains=city) for city in cities)
                        )
                    ),
                ),
            )
            qs = qs.filter(query)
        return qs
