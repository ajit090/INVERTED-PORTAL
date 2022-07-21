from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Battery,Complaint


class BatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Battery
        fields = '__all__' 

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__' 