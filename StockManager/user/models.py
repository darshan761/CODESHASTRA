from django.db import models

# Create your models here.


class Stocks(models.Model):

    name = models.CharField(max_length=200, help_text="Enter Stock Name")
    description = models.TextField(help_text="Enter Product Description")
    unitCost = models.FloatField(default=0.0,help_text="Enter Stock Unit Cost")
    unit = models.CharField(max_length=10,help_text="Enter Stock Unit ")
    quantity = models.FloatField(default=0.0,help_text="Enter Stock Quantity")
    minQuantity = models.FloatField(default=0.0,help_text="Enter Stock Min Quantity")
    open = models.FloatField(default=0.0)
    high = models.FloatField(default=0.0)
    low = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class User(models.Model):

    name = models.CharField(max_length=200, help_text="Enter User Name")
    description = models.TextField(help_text="Enter User Description")
    stock_no = models.IntegerField(default=0)
    portfolio_val = models.IntegerField(default=0.0)
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


