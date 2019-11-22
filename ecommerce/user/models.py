from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    description = models.TextField()

    def __str__(self):
        return self.name
