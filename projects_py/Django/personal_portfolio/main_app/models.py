from django.db import models
from datetime import *

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=124)
    email = models.CharField(max_length=124)
    subject = models.CharField(max_length=124)
    message = models.TextField(max_length=1124)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
