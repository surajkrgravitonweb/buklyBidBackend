
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

# type(String),UserId (Null=true),hightestBidding(Null=true))
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
    Auction_type=models.CharField(max_length=200, default=False)
    User_id=models.CharField(max_length=200, null=True , default=False)
    hightestBiddingPrice=models.CharField(max_length=200,null=True ,default=False)
    quantity=models.CharField(max_length=200,null=True , default=False)
    format=models.CharField(max_length=200,null=True , default=False)
    location=models.CharField(max_length=200,null=True , default=False)
    img = models.ImageField(upload_to='images/',default=False)
    vehicleNumber= models.CharField(max_length=200, null=True, blank=True)
    experyDate= models.TimeField(null=True)


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
    Car_details = models.ManyToManyField(CarModel, blank=True, related_name='profiles')

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


# models.py
from django.db import models

class PremiumPayment(models.Model):
    Name = models.CharField(max_length=255)
    Mobile = models.CharField(max_length=15)
    CD = models.CharField(max_length=255)
    Email = models.EmailField()
    RegisteredId = models.CharField(max_length=255,null=True, blank=True)
    PaymentDetails = models.CharField(max_length=255)
    InterestedIn = models.CharField(max_length=255)
    RenewalFee = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    TotalAmount = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)


class RequestForRegistration(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    mobile=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    youAre=models.CharField(max_length=200)


class MyDataModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # Add other fields as necessary




class BulkData(models.Model):
    sr = models.CharField(max_length=255)
    deal_no = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    dealer_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    new_state = models.CharField(max_length=255)
    deal_date = models.DateField()
    segment = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    registration_no = models.CharField(max_length=255)
    mfg_year = models.IntegerField()
    engine_no = models.CharField(max_length=255)
    chassis_no = models.CharField(max_length=255)
    repo_date = models.DateField()
    vehicle_parked_with = models.CharField(max_length=255)
    yard_name = models.CharField(max_length=255)
    parked_at = models.CharField(max_length=255)
    yard_city = models.CharField(max_length=255)
    report = models.CharField(max_length=255)
    images = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.deal_no} - {self.customer_name}"



class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    interest = models.JSONField(default=list)

    def __str__(self):
        return self.username


class AccountReigster(models.Model):
    ADMIN = 1
    USER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (USER, 'User')
    )
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    fullname =models.CharField(max_length=200)
    email   =models.CharField(max_length=200,unique=True)
    phone_number=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=USER)

    # pancard =models.CharField(max_length=200)
    # bankaccount=models.CharField(max_length=200)
    # ifsccode=models.CharField(max_length=200)
    # aadhaarCardNumber=models.CharField(max_length=200)
    

# models.py
from django.db import models

class Payment(models.Model):
    name = models.CharField(max_length=255)
    user_phone_no = models.CharField(max_length=15)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    registered_id = models.CharField(max_length=255, blank=True, null=True)
    payment_of = models.CharField(max_length=20)
    interested_items = models.JSONField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.name
