from django.shortcuts import render
from django.http import HttpResponse
from .models import Bill

# Create your views here.
def index(request):
    all_bills = Bill.objects.all()
    return render(request, 'index.html', {
        "bills": all_bills
    })

def join(request):
    return render(request, 'join.html', {})