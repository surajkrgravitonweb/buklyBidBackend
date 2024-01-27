from django.contrib import admin
from .models import *
# Register your models here.

# from django.contrib.admin.models import LogEntry

# admin.site.register(User)/
admin.site.register(Contact)

admin.site.register(OTPVerifiaction)
admin.site.register(ServicesModel)
admin.site.register(CarModel)
admin.site.register(ProfileModel)
admin.site.register(UserProfile)
admin.site.register(BulkData)

