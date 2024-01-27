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


# serializers.py
from rest_framework import serializers
from .models import Bid

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'


# serializers.py
from rest_framework import serializers
from .models import Bid, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class BidingSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = Bidding
        fields = '__all__'



class PremiumPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumPayment
        fields = '__all__'



class RequestForRegistrationSerilizers(serializers.ModelSerializer):
    class Meta:
        model =RequestForRegistration
        fields ='__all__'


class MyDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyDataModel
        fields = '__all__'


class BulkDataSerilizers(serializers.ModelSerializer):
    class Meta:
        model = BulkData
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'phone', 'city', 'gender', 'interest']




from rest_framework import serializers
from .models import *

class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model=AccountReigster
        fields='__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'