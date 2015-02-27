from django.db import models
# Create your models here.

class Binnacle_entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=512)

    class Meta:
        ordering = ('created', )
