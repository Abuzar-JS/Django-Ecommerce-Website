from django.db import models

# Create your models here.
class Category(models.Model):
    c_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="store/images/")
    weight = models.CharField(max_length=40)
    quantity = models.IntegerField(default=5)
    description = models.CharField(max_length=300)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

class User(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    dob = models.CharField(max_length=40)

    def __str__(self):
        return self.name
