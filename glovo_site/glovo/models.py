from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    ROLE_CHOICES = (
        ('клиент', 'клиент'),
        ('курьер', 'курьер'),
        ('владелец магазина', 'владелец магазина'),
        ('администратор', 'администратор')
    )
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='клиент')

    def __str__(self):
        return self.username



class Category(models.Model):
    category_name = models.CharField(max_length=32 ,unique=True)

    def __str__(self):
        return f'{self.category_name}'




class Store(models.Model):
    store_name  = models.CharField(max_length=32, unique=True)
    description = models.TextField(null=True, blank=True)
    contact_info = PhoneNumberField()
    address = models.TextField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='stores')


    def __str__(self):
        return f'{self.store_name}, {self.owner}'




class Product(models.Model):
    product_name = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveSmallIntegerField(default=1)
    store = models.ManyToManyField(Store, related_name='product')
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.product_name} - {self.price}'

    def get_total_price(self):
        return self.product.price * self.quantity

class ProductCombo(models.Model):
    combo_name = models.CharField(max_length=32, unique=True)
    combo_image = models.ImageField(upload_to='combo_images')
    price = models.PositiveSmallIntegerField()
    description = models.TextField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='combos')


class ProductPhotos(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')


class Order(models.Model):
    client = models.ForeignKey(UserProfile, related_name='client', on_delete=models.CASCADE)
    products = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    STATUS_ORDER_CHOICES = [
        ('Ожидает обработки', 'Ожидает обработки'),
        ('В процессе доставки', 'В процессе доставки'),
        ('Доставлен', 'Доставлен'),
        ('Отменен', 'Отменен')
    ]
    status_order = models.CharField(max_length=32, choices=STATUS_ORDER_CHOICES, default='Доставлен')
    delivery_address = models.CharField(max_length=32)
    courier = models.ForeignKey(UserProfile, related_name='courier', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} - {self.delivery_address}'



class Courier(models.Model):
    user = models.ForeignKey(UserProfile, related_name='users', on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('доступен', 'доступен'),
        ('занят', 'занят'),
    )
    status = models .CharField(max_length=32, choices=STATUS_CHOICES, default='доступен')
    current_order = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.status}'


class Review(models.Model):
    client = models.ForeignKey(UserProfile, related_name='user_client', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, related_name='store_store', on_delete=models.CASCADE)
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.client} - {self.store}'
