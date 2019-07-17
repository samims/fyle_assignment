from .models import Banks, Branches
from rest_framework import serializers


class BankSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = '__all__'


class BranchSerializers(serializers.ModelSerializer):
    bank = BankSerializers(read_only=True)

    class Meta:
        model = Branches
        fields = '__all__'
