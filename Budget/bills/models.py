from django.db import models

# Create your models here.
class Bill(models.Model):

    class Catergory(models.TextChoices):
        HOUSING = 'HOUSE', 'Housing'
        TRANSPORTATION = 'TRANS', 'Transportation'
        UTILITIES = 'UTL', 'Utilities'
        INSURANCE = 'INS', 'Insurance'
        MEDICAL = 'MED', 'Medical'
        SAVING_INVESTING_DEBT = 'SID', 'Savings investment & debt'
        ENTERTAINMENT = 'ENT', 'Entertainment'
        MISCELLANEOUS = 'MISC', 'Miscellaneous'

    class BillFrequency(models.TextChoices):
        MONTHLY = 'MON', 'Monthly'
        BIWEEKLY = 'BW', 'biweekly'
        SEMIMONTHLY = 'SM', 'Semimonthly'
        WEEKLY = 'W', 'Weekly'
        ANNUAL = 'AN', 'Annually'

    bill_name = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    due_date = models.PositiveIntegerField()
    type = models.CharField(max_length=7, choices=Catergory.choices)
    frequency = models.CharField(max_length=3, choices=BillFrequency.choices)

    def __str__(self):
        return self.bill_name
