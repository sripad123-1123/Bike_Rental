from django.views.generic.list import ListView
from app.models import Rent
from django.shortcuts import render
from django.http import request
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from renting_bike.models import Bikes
from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import login_required

# Create your views here.

# #@login_required
# def rent_test(request):

#     bks = MotorBike.objects.all()
    


#     return render(request, 'rent.html',{'bks':bks})

@login_required
def rent(request):
    if request.method == 'POST':
        bname = request.POST.get('bname')
        bike_name = Bikes.objects.get(name = bname)
        renting_time = request.POST.get('renting_Time')
        # renting_time = request.POST['date1']
        submission_time = request.POST.get('submission_Time')
        total_time = request.POST.get('total_time')
        total_amount = request.POST.get('total_amount')
        print("request.POST", request.POST)
        bike_rent = Rent.objects.create(bike=bike_name,user=request.user,start_time = renting_time,end_time = submission_time,total_time=total_time,total_cost = total_amount)
       
        bike_rent.save()
        return redirect('rented',bike_rent.id)
    else:
        return redirect('rent')

def rented(request,pk1):
    book = Rent.objects.get(id=pk1)
    context = {'book':book}
    return render(request,'rented.html',context)

# class rented(DetailView):
#     model = Rent
#     template_name = 'rented.html'

@login_required
def history(request):
    history = Rent.objects.filter(user=request.user).order_by("-id")

    return render(request,'history.html',{"history":history})

    