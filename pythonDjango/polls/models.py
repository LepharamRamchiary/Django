from django.db import models
from django.utils import timezone

# Create your models here.
class TeaVarity(models.Model):
    TEA_TYPE = [
        ('ML', 'Milk Tea'),
        ('GR', 'Ginger Tea'),
        ('BL', 'Black Tea'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tea/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=TEA_TYPE)
    desc = models.TextField(default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
