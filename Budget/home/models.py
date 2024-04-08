from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Income(models.Model):

    class Type(models.TextChoices):
        SALARY = 'Sal', 'Salary'
        VARIABLE = 'Var', 'Variable'
    
    class PayFrequency(models.TextChoices):
        MONTHLY = 'MON', 'Monthly'
        BIWEEKLY = 'BW', 'Bi-weekly'
        SEMIMONTHLY = 'SM', 'Semimonthly'
        WEEKLY = 'W', 'Weekly'
        ANNUAL = 'AN', 'Annually'

    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        primary_key=True,
    )
    pay_amount = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    type = models.CharField(max_length=3, choices=Type.choices)
    frequncy = models.CharField(max_length=3, choices=PayFrequency.choices)
    #Need day of the month, to calculate weekly, bi-weekly and monthly pay days
    pay_date_one = models.IntegerField(
        validators=[MaxValueValidator(31), MinValueValidator(1)]
     )
    #Need second date to calculate semi monthly(2x a month, so need both dates)
    pay_date_two = models.IntegerField(
        validators=[MaxValueValidator(28), MinValueValidator(1)], null=True, blank=True
     )

    def __str__(self):
        return f"{self.user} Income"