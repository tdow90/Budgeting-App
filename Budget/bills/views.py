from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bill
from .forms import BillForm

#Create your views here.
def index(request):
    all_bills = Bill.objects.all()
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
        "bills": all_bills, 
        "form": form
    })
    
