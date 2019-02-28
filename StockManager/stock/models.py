from django.db import models

# Create your models here.

class Stocks(models.Model):

    name = models.CharField(max_length=200, help_text="Enter Stock Name")
    description = models.TextField(help_text="Enter Product Description")

    unitCost = models.FloatField(help_text="Enter Stock Unit Cost")
    unit = models.CharField(max_length=10,help_text="Enter Stock Unit ")

    quantity = models.FloatField(help_text="Enter Stock Quantity")
    minQuantity = models.FloatField(help_text="Enter Stock Min Quantity")

    User = models.ForeignKey('User',on_delete=models.CASCADE,)
    #location = models.ForeignKey('Location')

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Product.
        """
        return reverse('stock-detail-view', args=[str(self.id)])

    def __str__(self):

        return self.name
