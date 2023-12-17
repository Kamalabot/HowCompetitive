from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=50)


# multiple product can be supplied to a single Customer
class Products(models.Model):
    pdt_name = models.CharField(max_length=200)
    cost = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"name:{self.pdt_name}, cost:{self.cost}, quantity:{self.quantity} \n"
