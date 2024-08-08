from django.db import models

class Products(models.Model):
    product_name        = models.CharField(max_length=50)
    product_description = models.TextField()
    product_price       = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock       = models.IntegerField()