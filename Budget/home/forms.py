from django.forms import ModelForm
from .models import Income

class IncomeForm(ModelForm):
    class Meta: 
        model = Income
        fields = ["pay_amount", "type", "frequency", "pay_date_one", "pay_date_two"]
        