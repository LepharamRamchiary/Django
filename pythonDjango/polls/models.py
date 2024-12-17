from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

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
    

# One to Many 
class TeaReview(models.Model):
    tea = models.ForeignKey(TeaVarity, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # rating = models.IntegerField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating should be between 1 (lowest) and 5 (highest)."
    )
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username} review for {self.tea.name}"
    
# many to many 
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    tea_varieties = models.ManyToManyField(TeaVarity, related_name="stores")
    
    def __str__(self):
        return self.name
    

#one to one 
class TeaCertificate(models.Model):
    tea = models.OneToOneField(TeaVarity, on_delete=models.CASCADE, related_name="certificate")
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateField(default=timezone.now)
    valid_date = models.DateField()
    
    def __str__(self):
        return f'Certificate for {self.tea.name}'