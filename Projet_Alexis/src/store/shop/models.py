from django.db import models
from django.urls import reverse
from store.settings import AUTH_USER_MODEL
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    def __str__(self):
        return f'{self.title} ({self.price})'
    
    '''    def get_absolute_url(self): # get url and add button on admin
        return f"/products/{self.slug}" '''

    def get_absolute_url(self): # get url from path on urls.py add button on admin
        return reverse("product", kwargs={"slug": self.slug})
    

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.product.title} ({self.quantity})"

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.user.username
    
    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()
        self.orders.clear()    

        super().delete(*args, **kwargs)
