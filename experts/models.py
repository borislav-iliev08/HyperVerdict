from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from accounts.models import Profile


# Create your models here.
class ExpertsListing(models.Model):
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    specialization = models.ManyToManyField("Specializations",related_name='specializations')
    experience_years = models.PositiveIntegerField(validators=[MaxValueValidator(50),MinValueValidator(1)])
    consultation_price = models.DecimalField(max_digits=5,decimal_places=2,validators=[MinValueValidator(1.00)])
    city = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Specializations(models.Model):
    class CategoryChoices(models.TextChoices):
        RE = 'Real Estate','Real Estate'
        LA = 'Legal','Legal'
    name = models.CharField(max_length=50,unique=True)
    category = models.CharField(max_length=12,choices=CategoryChoices.choices)
    description = models.TextField(max_length=200)



