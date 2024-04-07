from django.forms import ModelForm
from .models import Bill

class BillForm(ModelForm):
    class Meta:
        model = Bill
        fields = ["bill_name", "amount", "due_date", "type", "frequency"]
