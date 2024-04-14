from django.shortcuts import render, redirect
from bills.models import Bill
from .models import Income
from django.contrib.auth.decorators import login_required
from .forms import IncomeForm

# Create your views here.
@login_required()
def index(request):
    income = Income.objects.filter(user=request.user)
    bills = Bill.objects.filter(user=request.user)

    bill_amount=0
    pay_total = 0
    for bill in bills:
        bill_amount = bill_amount + bill.amount
    
    for i in income:
        pay_total = pay_total + i.pay_amount
    money_left = pay_total - bill_amount

    return render(request, "home/home.html", { 
        "income": income, 
        "bills": bills,
        "bill_amount": bill_amount,
        "money_left": money_left,
    })

@login_required()
def income(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user 
            form.save()

    else:
        form = IncomeForm()        
    return render(request, 'home/income.html', {
        "form": form
    })

def profile(request):
    pass