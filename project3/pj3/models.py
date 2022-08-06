from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    linkedin = models.URLField(max_length=122)
    twitter = models.URLField(max_length=122)
    instagram = models.URLField(max_length=122)

    def __str__(self):
        return self.name
