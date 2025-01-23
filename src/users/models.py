from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Location(models.Model):
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    

    

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    photo= models.ImageField(blank=True)
    bio= models.CharField(max_length=14,blank=True)
    phone_number=models.CharField(max_length=12,blank=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
