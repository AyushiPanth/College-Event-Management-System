from django.db import models

# Create your models here.
from django.urls import reverse
class Club(models.Model):
    club_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length = 255)

    def get_absolute_url(self):
        return reverse("club:index")
    
    