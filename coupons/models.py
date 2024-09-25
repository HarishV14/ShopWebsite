from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    # validation function that check the validity of input value not less that 0 not greater than 100
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    active = models.BooleanField()
    def __str__(self):
        return self.code