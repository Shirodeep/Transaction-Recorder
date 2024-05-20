from django.shortcuts import render, redirect
from home.models import *
# Create your views here.
def home(request):
    uname = request.session.get('uname')
    data = []
    if uname:
        try:
            all = Debit.objects.filter(user_id=int(request.user.id))
            counter = 0
            for i in all:
                if counter == 14:
                    break
                data.append({
                    'id': i.id,
                    'name': i.name,
                    "amount": i.amount,
                    'is_gain': int(i.is_gain),
                    'user': i.user
                })            
                counter += 1
        except: 
            pass
    return render(request, 'home.html', {'page_title': 'Home', 'data': data})

def about(request):
    return render(request, 'aboutus.html', {'page_title': 'About'})

def add_items(request):
    if request.session.get('uname'):
        try:
            if request.method == "POST":
                name = request.POST.get('name')
                amount = request.POST.get('amount')
                is_gain = request.POST.get('is_gain')
            debit = Debit(name= name, amount= amount, is_gain= is_gain,  user= request.user)
            debit.save()
            return redirect('../')
        except:
            pass
    return render(request, 'additems.html')


def details(request, id):
    data = {}
    if request.session.get('uname'):    
        try: 
            item = Debit.objects.get(id = id)
            data = {
                'item': item
            }
        except:
            pass
    return render(request, 'detailview.html', data)


def remove_item(request, id):
    if request.session.get('uname'):
        try: 
            item = Debit.objects.get(id = id, user_id= request.user).delete()
            return redirect('home')
        except:
            pass
    return redirect('home')

def update_items(request, id):
    if request.session.get('uname'):
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
