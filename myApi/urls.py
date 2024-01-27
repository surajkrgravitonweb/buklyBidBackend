from django.urls import path
from .views import (
    create_contact,
    list_contacts,
    retrieve_contact,
    update_contact,
    delete_contact,
)
from .views import *
urlpatterns = [

    path('upload_deals/', upload_deals, name='upload_deals'),
    path('get_deals/', get_deals, name='get_deals'),
    path('upload_excel/', ExcelUploadView.as_view(), name='upload-excel'),

    path('request/', RequestForRegistrationViewSet.as_view(), name='RequestForRegistrationViewSet'),

    path('bulkupload_excel/', BulkDataView.as_view(), name='upload-excel'),
    path('bulkupload_excel/<int:pk>/', BulkDataView.as_view(), name='details-excel'),

  
    path('accounts/', RegisterAPIView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', RegisterAPIView.as_view(), name='account-detail'),
    path('login/', UserLoginView.as_view(), name='login'),



    path('premiuePayment/', PremiumPaymentListCreateView.as_view(), name='Premium Payment List Create View'),
    path('premiuePayment/<int:pk>/', PremiumPaymentListCreateView.as_view(), name='Premium Payment List Deatils View'),


    path('bidding/', bid_list, name='bid-list'),
    path('bidding/<int:bid_id>/', bid_detail, name='bid-detail'),

    path('place_bid/', place_bid, name='place-bid'),
    path('get_highest_bid/<int:item_id>/', get_highest_bid, name='get-highest-bid'),



    path('create/', create_contact, name='create_contact'),
    path('list/', list_contacts, name='list_contacts'),
    path('retrieve/<int:pk>/', retrieve_contact, name='retrieve_contact'),
    path('update/<int:pk>/', update_contact, name='update_contact'),
    path('delete/<int:pk>/', delete_contact, name='delete_contact'),

    path('checkOTP/', checkOTP ),
    path('sendOTP/',otpGeneration),


    path('services/create/', create_service, name='create_service'),
    path('services/list/', list_services, name='list_services'),
    path('services/retrieve/<int:pk>/', retrieve_service, name='retrieve_service'),
    path('services/update/<int:pk>/', update_service, name='update_service'),
    path('services/delete/<int:pk>/', delete_service, name='delete_service'),


    path('carmodels/create/', create_car_model, name='create_car_model'),
    path('carmodels/list/', list_car_models, name='list_car_models'),
    path('carmodels/retrieve/<int:pk>/', retrieve_car_model, name='retrieve_car_model'),
    path('carmodels/partial_update/<int:pk>/', partial_update_car_model, name='partial_update_car_model'),
    path('carmodels/update/<int:pk>/', update_car_model, name='update_car_model'),
    path('carmodels/delete/<int:pk>/', delete_car_model, name='delete_car_model'),

     path('profiles/create/', create_profile_model, name='create_profile_model'),
    path('profiles/list/', list_profile_models, name='list_profile_models'),
    path('profiles/retrieve/<int:pk>/', retrieve_profile_model, name='retrieve_profile_model'),
    path('profiles/update/<int:pk>/', update_profile_model, name='update_profile_model'),
    path('profiles/delete/<int:pk>/', delete_profile_model, name='delete_profile_model'),


    path('api/profiles/', UserProfileListCreateView.as_view(), name='profile-list-create'),
    path('api/profiles/<int:pk>/', UserProfileDetailView.as_view(), name='profile-detail'),

     path('api/payment/', PaymentDetailsView.as_view(), name='payment-list'),
    path('api/payment/<int:pk>/', PaymentDetailsView.as_view(), name='payment-detail'),

     path("emailNewRegistratinos/", SendmailRegistrations.as_view(), name = "emailNewRegistratinos"),


]


