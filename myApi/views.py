from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import *
from .serializers import ContactSerializer

@api_view(['POST'])
def create_contact(request):
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Contact created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"message": "Failed to create contact", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_contacts(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response({"message": "Contact list retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def retrieve_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    serializer = ContactSerializer(contact)
    return Response({"message": "Contact retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    serializer = ContactSerializer(contact, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Contact updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
    return Response({"message": "Failed to update contact", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return Response({"message": "Contact deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




import requests
import random
import math
def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP
def generatingOTP(number):
    OTP = generateOTP()

    return OTP
url = "https://www.fast2sms.com/dev/bulkV2"
@api_view(['GET', 'POST'])
def otpGeneration(request):
    number = request.data['number']
    print(number)
    generatedOTP = generatingOTP(number)
    print(generatedOTP)
    s=OTPVerifiaction.objects.filter(phone_number=number).delete()
    print("end")
    querystring = {"authorization":"FlksSDzg13vfLoUreKH9xh6CbXIA42OVynQduMPG0Bm7Ja5c8qdaBRD5fUS4lT0EX2HzV9rtAcInkZxK","variables_values":generatedOTP,"route":"otp","numbers":number}
    headers = {
    'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print("start")
    print(response.text)
    if generatedOTP:
        data = OTPVerifiaction(phone_number=number, otp=generatedOTP)
        data.save()
        print(generatedOTP)
        return Response({"OTPSent": True})
    else:
        return Response({"OTPSent": False})


@api_view(['PUT'])
def checkOTP(request):
    number = request.data['number']
    otp = request.data['otp']
    print("checking time",number,otp)
    generatedOTP = OTPVerifiaction.objects.filter(
        phone_number=number).values_list('otp')
    print(generatedOTP)
    if generatedOTP[0][0] == otp:
        data = OTPVerifiaction.objects.get(phone_number=number)
        data.is_verfied = True
        data.save()
        return Response({"status": True})

    else:
        return Response({"status": False})



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ServicesModel
from .serializers import ServicesModelSerializer

@api_view(['POST'])
def create_service(request):
    serializer = ServicesModelSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Service created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"message": "Failed to create service", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_services(request):
    services = ServicesModel.objects.all()
    serializer = ServicesModelSerializer(services, many=True)
    return Response({"message": "Service list retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def retrieve_service(request, pk):
    service = ServicesModel.objects.get(pk=pk)
    serializer = ServicesModelSerializer(service)
    return Response({"message": "Service retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_service(request, pk):
    service = ServicesModel.objects.get(pk=pk)
    serializer = ServicesModelSerializer(service, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Service updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
    return Response({"message": "Failed to update service", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_service(request, pk):
    service = ServicesModel.objects.get(pk=pk)
    service.delete()
    return Response({"message": "Service deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CarModel
from .serializers import CarModelSerializer

@api_view(['POST'])
def create_car_model(request):
    serializer = CarModelSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Car model created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"message": "Failed to create car model", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_car_models(request):
    car_models = CarModel.objects.all()
    serializer = CarModelSerializer(car_models, many=True)
    return Response({"message": "Car model list retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def retrieve_car_model(request, pk):
    car_model = CarModel.objects.get(pk=pk)
    serializer = CarModelSerializer(car_model)
    return Response({"message": "Car model retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_car_model(request, pk):
    car_model = CarModel.objects.get(pk=pk)
    serializer = CarModelSerializer(car_model, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Car model updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
    return Response({"message": "Failed to update car model", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_car_model(request, pk):
    car_model = CarModel.objects.get(pk=pk)
    car_model.delete()
    return Response({"message": "Car model deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ProfileModel
from .serializers import ProfileModelSerializer

@api_view(['POST'])
def create_profile_model(request):
    serializer = ProfileModelSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Profile created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"message": "Failed to create profile", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_profile_models(request):
    profile_models = ProfileModel.objects.all()
    serializer = ProfileModelSerializer(profile_models, many=True)
    return Response({"message": "Profile list retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def retrieve_profile_model(request, pk):
    profile_model = ProfileModel.objects.get(pk=pk)
    serializer = ProfileModelSerializer(profile_model)
    return Response({"message": "Profile retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_profile_model(request, pk):
    profile_model = ProfileModel.objects.get(pk=pk)
    serializer = ProfileModelSerializer(profile_model, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Profile updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
    return Response({"message": "Failed to update profile", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_profile_model(request, pk):
    profile_model = ProfileModel.objects.get(pk=pk)
    profile_model.delete()
    return Response({"message": "Profile deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Deal

@csrf_exempt  # Only if you choose CSRF exemption or use ensure_csrf_cookie decorator
def upload_deals(request):

    if request.method == 'POST':
        try:
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)

            for _, row in df.iterrows():
                Deal.objects.create(
                    deal_no=row['Deal No'],
                    brand=row['Brand'],
                    model=row['Model'],
                    new_state=row['New State'],
                    location=row['Location'],
                    deal_date=row['Deal Date'],
                    customer_name=row['Customer Name'],
                    registration_no=row['Registration No'],
                    rc_available=row['Rc Available'],
                    repo_date=row['Repo Date'],
                    segment=row['Segment'],
                    parked_at=row['Parked At'],
                    yard_city=row['Yard City'],
                    valuation_amount=row['Valuation Amount'],
                    valuation_report_link=row['Valuation Report Link'],
                    manufacturing_year=row['Manufacturing Year'],
                    base_rate=row['Base rate']
                )

            return JsonResponse({'message': 'Data uploaded successfully'})
        except Exception as e:
            return JsonResponse({'error': f'Error uploading data: {str(e)}'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)





from django.http import JsonResponse

from .models import Deal

from django.core import serializers
 
def get_deals(request):

    if request.method == 'GET':

        deals = Deal.objects.all()

        data = serializers.serialize('json', deals)

        return JsonResponse({'deals': data})

    return JsonResponse({'error': 'Invalid request'}, status=400)





# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Bid
from .serializers import BidSerializer

@api_view(['GET', 'POST'])
def bid_list(request):
    if request.method == 'GET':
        bids = Bid.objects.all()
        serializer = BidSerializer(bids, many=True)
        return Response({"message": "Bids retrieved successfully", "status": "success", "data": serializer.data})

    elif request.method == 'POST':
        serializer = BidSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Bid created successfully", "status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Invalid data", "status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def bid_detail(request, bid_id):
    try:
        bid = Bid.objects.get(pk=bid_id)
    except Bid.DoesNotExist:
        return Response({"message": "Bid not found", "status": "error"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BidSerializer(bid)
        return Response({"message": "Bid retrieved successfully", "status": "success", "data": serializer.data})

    elif request.method == 'PUT':
        serializer = BidSerializer(bid, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Bid updated successfully", "status": "success", "data": serializer.data})
        return Response({"message": "Invalid data", "status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bid.delete()
        return Response({"message": "Bid deleted successfully", "status": "success"})



# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Bid, Item
from .serializers import BidingSerializer, ItemSerializer

@api_view(['POST'])
def place_bid(request):
    serializer = BidingSerializer(data=request.data)
    if serializer.is_valid():
        # Check if the bid is higher than the current highest bid for the item
        item_id = serializer.validated_data['item']['id']
        current_highest_bid = Bidding.objects.filter(item_id=item_id).order_by('-amount').first()

        if current_highest_bid is None or serializer.validated_data['amount'] > current_highest_bid.amount:
            serializer.save()
            return Response({"message": "Bid placed successfully", "status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Bid amount is not higher than the current highest bid", "status": "error"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Invalid data", "status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_highest_bid(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        return Response({"message": "Item not found", "status": "error"}, status=status.HTTP_404_NOT_FOUND)

    highest_bid = Bidding.objects.filter(item=item).order_by('-amount').first()

    if highest_bid:
        serializer = BidingSerializer(highest_bid)
        return Response({"message": "Highest bid retrieved successfully", "status": "success", "data": serializer.data})
    else:
        return Response({"message": "No bids for this item", "status": "success"})
