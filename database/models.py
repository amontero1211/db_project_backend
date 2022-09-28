from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=20)
    image = models.CharField(max_length=200)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    nationality = models.CharField(max_length=12)
    commission = models.DecimalField(max_digits=4, decimal_places=2)
    biography = models.TextField()


class ArtWork(models.Model):

    STATES = [
        ('available','Disponible'),
        ('reserved','Reservado'),
        ('sold_out','Vendido'),
    ]

    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, null=True)
    genre = models.CharField(max_length=15, null=True)
    create_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    image = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=10, choices=STATES, default='available')
    

class Invoice(models.Model):
    artWork_id = models.OneToOneField(ArtWork, on_delete=models.CASCADE, parent_link=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    price_total = models.DecimalField(max_digits=10, decimal_places=2)


class Purchaser(User):
    card_number = models.CharField(max_length=16)
    card_back_number = models.CharField(max_length=3)
    card_expiration_date = models.DateField(auto_now=False, auto_now_add=False)
    purchase_key = models.CharField(max_length=6, null=True)
    question_1 = models.CharField(max_length=30, null=True)
    question_2 = models.CharField(max_length=30, null=True)
    question_3 = models.CharField(max_length=30, null=True)
    answer_1 = models.CharField(max_length=30, null=True)
    answer_2 = models.CharField(max_length=30, null=True)
    answer_3 = models.CharField(max_length=30, null=True)