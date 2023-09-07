from django.shortcuts import render,redirect
from item.models import *
import csv
from django.http import HttpResponse
from .forms import Sighnupform
# Create your views here.

def index(request):
    items = Items.objects.filter(is_sold=False)[:6]
    category = Category.objects.all()
    context ={
        'categories': category,
        'items': items
    }
    return render(request,"core/index.html",context)

def contacts(request):
    return render(request,"core/contacts.html")

def csv_import(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Price', 'Description'])  # Add appropriate headers

    items = Items.objects.filter(is_sold=False)  # Replace with your queryset
    for item in items:
        writer.writerow([item.name, item.price, item.description])  # Add corresponding data

    return response

def sighnup(request):
    print("request.method",request.method)
    if request.method == 'POST':
        form = Sighnupform(request.POST)
        print("form",form)

        if form.is_valid():
            form.save()

            return redirect('/login')
    else:
        print("inselse")
        form = Sighnupform()
    return render(request,"core/sighnup.html",{'form': form})



