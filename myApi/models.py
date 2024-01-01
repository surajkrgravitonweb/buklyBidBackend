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
    rc_available =models.BooleanField(default=False)

    def __str__(self):
        return self.model_name

from django.db import models

class ProfileModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    verification = models.BooleanField(default=False)
    aadhar = models.ImageField(upload_to='images/',default=False)
    panCard = models.ImageField(upload_to='images/' ,default=False)

    def __str__(self):
        return self.name


from django.db import models
 
class Deal(models.Model):
    deal_no = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=200)
    new_state = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    deal_date = models.DateField()
    customer_name = models.CharField(max_length=200)
    registration_no = models.CharField(max_length=100, null=True, blank=True)  
    rc_available = models.CharField(max_length=3, choices=[('YES', 'Yes'), ('NO', 'No')])
    repo_date = models.DateField()
    segment = models.CharField(max_length=100)
    parked_at = models.TextField()
    yard_city = models.CharField(max_length=100)
    valuation_amount = models.FloatField()
    valuation_report_link = models.URLField(max_length=500)
    manufacturing_year = models.IntegerField()
    base_rate = models.FloatField()
 
    def __str__(self):
        return self.deal_no
    

class Bid(models.Model):
    userId = models.IntegerField()
    CarId = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)



# models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)

class Bidding(models.Model):
    user_id = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
