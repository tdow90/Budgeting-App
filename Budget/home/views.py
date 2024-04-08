from django.shortcuts import render
from bills.models import Bill
from .models import Income

# Create your views here.
def index(request):
    income = Income.objects.filter(user=request.user)
    bills = Bill.objects.filter(user=request.user)
    return render(request, "home/home.html", { 
        "income": income, 
        "bills": bills,
    })