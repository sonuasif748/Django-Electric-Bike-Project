from django.db import models
from django.contrib.auth.models import User
# User._meta.get_field('email')._unique =True

class cust(models.Model):
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (FeMale, 'Female'),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    state = models.CharField(max_length=40,null=False)
    country = models.CharField(max_length=40)
    pincode = models.CharField(max_length=20,null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,
                              default=Male)
    time = models.DateTimeField(auto_now_add=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name
class dealer(models.Model):
    STATUS = (
        ('ONLINE', 'ONLINE'),
        ('OFFLINE', 'OFFLINE'),
    )
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (FeMale, 'Female'),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=40)
    shop_address = models.CharField(max_length=40)
    dealer_type = models.CharField(max_length=40,choices=STATUS)

    profile_pic1= models.ImageField(upload_to='profile_pic/dealerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    pincode = models.CharField(max_length=20,null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,
                              default=Male)
    time = models.DateTimeField(auto_now_add=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name
    # def __str__(self):
    #     return self.user.username

#cust.......
class bike(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    working= 'Working'
    Not_working= 'Not Working'
    BIKE_CHOICES = (
        (working, '1'),
        (Not_working, '0'),
    )

    headlight=models.CharField(max_length=11,choices=BIKE_CHOICES,default=1)
    signal_light=models.CharField(max_length=11,choices=BIKE_CHOICES,default=1)
    breaks=models.CharField(max_length=11,choices=BIKE_CHOICES,default=1)
    motor_working=models.CharField(max_length=11,choices=BIKE_CHOICES,default=1)
    key=models.CharField(max_length=11,choices=BIKE_CHOICES,default=1)
    body_status=models.CharField(max_length=11,choices=BIKE_CHOICES,default=1)
    usb_status=models.CharField(max_length=11,choices=BIKE_CHOICES,default=1)
    battery=models.CharField(max_length=11,choices=BIKE_CHOICES,default=1)
    controller=models.CharField(max_length=11,choices=BIKE_CHOICES,default=1)


class kilometers(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField()
    Ridekm = models.CharField(max_length=20)
    useCharge = models.CharField(max_length=25)
    BalCharge = models.CharField(max_length=20)


class Recharge(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    BPercentage = models.CharField(max_length=3)
    RTime = models.TextField(max_length=20)
    KmsRide = models.IntegerField()

class estimatekms(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    BPercentage = models.CharField(max_length=3)
    KmsRide = models.IntegerField()


class Battery_status(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    charging_state = models.BooleanField()
    battery_level = models.PositiveIntegerField()
    dischrging_time = models.TimeField()


class Speedometer(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    speed = models.IntegerField()


class LockUnlock(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pin = models.CharField(max_length=4)


class Bikesales(models.Model):
    product_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=50, null=True)
    customer = models.ForeignKey(cust, on_delete=models.CASCADE, null=True)
    sales_per_day = models.IntegerField()
    total_sales = models.IntegerField()


#
# class bookbike(models.Model):
#     name = models.CharField(max_length=100)
#     number=models.CharField(max_length=100)
#     email=models.EmailField()
#     address = models.CharField(max_length=200)
#     pincode=models.CharField(max_length=100)
#     state=models.CharField(max_length=50)
#     bikename = models.CharField(max_length=100)
#     amount = models.CharField(max_length=100)
#     order_id = models.CharField(max_length=100, blank=True)
#     razorpay_payment_id = models.CharField(max_length=100, blank=True)
#     paid = models.BooleanField(default=False)
    #
    #
    # class Meta:
    #     # managed = True
    #     db_table = 'sgoapp_ebikes_bookbike'

# class bookbike(models.Model):
#     name = models.CharField(max_length=100)
#     number = models.CharField(max_length=100)
#     email=models.EmailField()
#     address = models.CharField(max_length=200)
#     pincode=models.CharField(max_length=100)
#     state=models.CharField(max_length=50)
#     bikename = models.CharField(max_length=100)
#     amount = models.CharField(max_length=100)
#     order_id = models.CharField(max_length=100, blank=True)
#     razorpay_payment_id = models.CharField(max_length=100, blank=True)
#     paid = models.BooleanField(default=False)
#     #
#     #
#     # class Meta:
#     #     # managed = True
#     #     db_table = 'sgoapp_ebikes_bookbike'


class shopnames(models.Model):
    shopnames = models.ForeignKey(dealer, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.shopnames
    def __str__(self):
        return str(self.shopnames)
    # def __str__(self):
    #     return f'Memo={self.shopnames}, Tag={self.shopnames}'
from django_countries.fields import CountryField
# from django.db.models import CountryField
class bookbike(models.Model):
    DEALER_CHOICES=(('dealer1','dealer1'),
    ('dealer2','dealer2'),('dealer3','dealer3'))
    SHOP_CHOICES=(('shop1','shop1'),
    ('shop2','shop2'))
    BIKEMODEL_CHOICES=(('TVS Jupiter','TVS Jupiter'),
    ('Hero HF Deluxe','Hero HF Deluxe'),
    ('Yamaha YZF R15 V3','Yamaha YZF R15 V3'),
    ('Bajaj Pulsar NS 125','Bajaj Pulsar NS 125'),
    ('Hero Splendor Plus','Hero Splendor Plus'),
    ('Yamaha MT-15','Yamaha MT-15'),
    ('Royal Enfield Classic 350','Royal Enfield Classic 350'),
    ('TVS Apache RTR 160','TVS Apache RTR 160'),
    ('Royal Enfield Bullet 350','Royal Enfield Bullet 350'),
    ('Bajaj Pulsar 150','Bajaj Pulsar 150'),
    ('Bajaj Pulsar NS200','Bajaj Pulsar NS200'),
    ('TVS Apache RTR 160 4V','TVS Apache RTR 160 4V'),
    ('Hero HF Deluxe','Hero HF Deluxe'),
    ('2021 Suzuki Hayabusa','2021 Suzuki Hayabusa'),
    ('TVS Apache RR 310','TVS Apache RR 310'),
    ('TVS Apache RTR 200 4V','TVS Apache RTR 200 4V'))
    CHOICES = (
        ('TVS Jupiter', (
            ('64437', '64437'),
            (12, '64437'),
            (13, 'Taxes'),
        )),
        ('Hero HF Deluxe', (
            ('38900', '38900'),
            ('63175', '63175'),
        )),
        ('Yamaha YZF R15 V3', (
            ('141000', '141000'),
            ('158000', '158000'),
        )),
        ('Hero Splendor Plus',(
            ('49990 ','49990 '),
            ('68560','68560'),
            ('59870','59870')
        )),
        ('Yamaha MT-15',(
            ('140000','140000'),
            ('141000','141000')
        )),
        ('Royal Enfield Classic 350',(
            ('152000','152000'),
            ('200000','200000'),
            ('217000','217000')
        )),
        ('TVS Apache RTR 160',(
            ('103000','103000'),
            ('106000','106000')
        ))
    )
    BIKEPRICE_CHOICES=(('64437','TVS Jupiter '),('73737','Yamaha YZF R15 V3'),('15200  ','Bajaj Pulsar NS 125 '),
    ('93690','Hero Splendor Plus'),('62535','Yamaha MT-15'),('140000 ','Royal Enfield Classic 350'),
    ('18000','Bajaj Pulsar 150'),('19800','Bajaj Pulsar NS200'))
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email=models.EmailField()
    address = models.CharField(max_length=200)
    pincode=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    country = CountryField()
    dealer_name = models.ForeignKey(shopnames, on_delete=models.SET_NULL, null=True)

    # dealer_name=models.ForeignKey(dealer,on_delete=models.CASCADE)
    # shopname=models.foreignKey()
    bikename = models.CharField(max_length=100,choices= BIKEMODEL_CHOICES,default=None)
    amount = models.CharField(max_length=100,choices=CHOICES,default=None)
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    #
    #
    # class Meta:
    #     # managed = True
    #     db_table = 'sgoapp_ebikes_bookbike'
class adminvisit(models.Model):
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (FeMale, 'Female'),
    )
    dealer_name = models.ForeignKey(dealer,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,
                              default=Male)
    mobile_no=models.BigIntegerField()
    address = models.CharField(max_length=100)
    pincode=models.BigIntegerField()
    bikename = models.CharField(max_length=200)
    purpose = models.CharField(max_length=100)
