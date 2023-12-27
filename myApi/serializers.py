from rest_framework import serializers
from .models import *

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'



class ServicesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesModel
        fields = '__all__'



class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = '__all__'
