from django.shortcuts import render, redirect
from home.models import *

# Create your views here.
def home(request):
    data = []
    try:
        all = Debit.objects.all()
        counter = 0
        for i in all:
            if counter == 14:
                break
            data.append({
                'id': i.id,
                'name': i.name,
                "amount": i.amount,
                'is_gain': int(i.is_gain)
            })            
            counter += 1
    except: 
        pass
    return render(request, 'home.html', {'page_title': 'Home', 'data': data})

def about(request):
    return render(request, 'aboutus.html', {'page_title': 'About'})

def add_items(request):
    data = {}
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            amount = request.POST.get('amount')
            is_gain = request.POST.get('is_gain')

        data = {
            'name': name,
            'amount': amount,
            'is_gain': is_gain
        }
        debit = Debit.objects.create(**data)
        return redirect('../')
    except:
        pass
    return render(request, 'additems.html')


def details(request, id):
    data = {}
    try: 
        item = Debit.objects.get(id = id)
        data = {
            'item': item
        }
    except:
        pass
    return render(request, 'detailview.html', data)


def remove_item(request, id):
    try: 
        item = Debit.objects.get(id = id).delete()
        return redirect('home')
    except:
        pass
    return redirect('home')

def update_items(request, id):
    try:
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        
        debit = Debit.objects.get(id = id)
        debit.name = name
        debit.amount = amount
        debit.save()
        return redirect(f'/detail/{id}')
    except:
        pass
    return redirect(f'/detail/{id}')
