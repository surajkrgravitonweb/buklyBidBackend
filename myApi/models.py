from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class OTPVerifiaction(models.Model):
    phone_number = models.IntegerField()
    otp = models.CharField(max_length=4)
    is_verfied = models.BooleanField(default=False)




class ServicesModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    time = models.DateTimeField()

    def __str__(self):
        return self.title
    



class CarModel(models.Model):
    model_name = models.CharField(max_length=255)
    buy_date = models.DateField()
    rc = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle_type = models.CharField(max_length=50)
    insurance = models.BooleanField(default=False)
    ownership = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.model_name

from django.db import models

class ProfileModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    verification = models.BooleanField(default=False)

    def __str__(self):
        return self.name

