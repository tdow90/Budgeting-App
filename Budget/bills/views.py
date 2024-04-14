from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bill
from .forms import BillForm
from django.contrib.auth.decorators import login_required

#Create your views here.
@login_required()
def index(request):
    bills = Bill.objects.filter(user=request.user)
    if request.method == "POST":
        form = BillForm()
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = BillForm(request.POST)
                form.instance.user = request.user    
            else:
                bill = Bill.objects.get(id=pk)
                form = BillForm(request.POST, instance=bill)
            if form.is_valid():
                form.save()
                form = BillForm()
                
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            bill = Bill.objects.get(id=pk)
            bill.delete()
            form = BillForm()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            bill = Bill.objects.get(id=pk)
            form = BillForm(instance=bill)

    else:
        form = BillForm()
    return render(request, 'bills/bills.html', {
        "bills": bills, 
        "form": form
    })
    
