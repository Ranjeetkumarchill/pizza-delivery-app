from django.db import models

# Create your models here.
class pizzaModel(models.Model):
	name=models.CharField(max_length=40)
	price=models.CharField(max_length=10)
    def __str__(self):
		return "({self.id}): {self.name}:{self.price}"


class CustomerModel(models.Model):
	userid=models.CharField(max_length=40)
	phoneno=models.CharField(max_length=20)

class OrderModel(models.Model):
	username=models.CharField(max_length=40)
	phoneno=models.CharField(max_length=20)
	address=models.CharField(max_length=50)
	ordereditems=models.CharField(max_length=20)
	status = models.CharField(max_length = 10)
