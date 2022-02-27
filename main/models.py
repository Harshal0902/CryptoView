from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class nft(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='nfts')
    price = models.CharField(max_length=100)
