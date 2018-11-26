from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator
from Restaurants.models import Restaurant, FoodCategory, Food
from Delivery.models import Delivery
# Create your models here.

Areas=(('Thames', 'Thames'),
       ('Lambeth', 'Lambeth'),
       ('Southpark', 'Southpark'),
       ('Nova', 'Nova'))


class Profile(models.Model):
    Customer_ID = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Customer_FName = models.CharField(max_length=200)
    Customer_LName = models.CharField(max_length=200)
    Customer_Num = models.CharField(max_length=10, unique=True)
    # Customer_Pic = models.ImageField(upload_to='Customers/Pictures/Profiles')
    Customer_Email = models.EmailField(default="asd@rew.com")

    def __str__(self):
        return self.user.username


class Address(models.Model):
    Address_ID = models.AutoField(primary_key=True)
    Customer_ID = models.ForeignKey(Profile, on_delete=models.CASCADE)
    #username = models.ManyToOneRel( )
    #username=models.CharField(max_length=200)
    Home = models.CharField(max_length=250)
    Society = models.CharField(max_length=250)
    Area = models.CharField(max_length=250, choices=Areas)
    City = models.CharField(max_length=250)
    State = models.CharField(max_length=250)
    Pin = models.CharField(max_length=6, default=000000)

    def __str__(self):
        return self.Area + ' ' + self.City


class Order(models.Model):
    Order_ID = models.AutoField(primary_key=True)
    Order_Customer_ID = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Order_Restaurant_ID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Order_Delivery_ID = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    Order_Status = models.IntegerField(MaxValueValidator(5))
    Order_Time = models.DateTimeField(default=timezone.now)
    # Order_Discount =
    # Order_Total_Price =


class Item(models.Model):
    Item_ID = models.AutoField(primary_key=True)
    Item_Order_ID = models.ForeignKey(Order, on_delete=models.CASCADE)
    Item_Food_ID = models.ForeignKey(Food, on_delete=models.CASCADE)
    Item_Quantity = models.IntegerField(MaxValueValidator(10))
    # Item_Price =
