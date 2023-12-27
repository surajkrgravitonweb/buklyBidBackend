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
    path('carmodels/update/<int:pk>/', update_car_model, name='update_car_model'),
    path('carmodels/delete/<int:pk>/', delete_car_model, name='delete_car_model'),

     path('profiles/create/', create_profile_model, name='create_profile_model'),
    path('profiles/list/', list_profile_models, name='list_profile_models'),
    path('profiles/retrieve/<int:pk>/', retrieve_profile_model, name='retrieve_profile_model'),
    path('profiles/update/<int:pk>/', update_profile_model, name='update_profile_model'),
    path('profiles/delete/<int:pk>/', delete_profile_model, name='delete_profile_model'),

]


