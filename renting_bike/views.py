from accounts.views import login
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Bikes
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator

# Create your views here.

# @login_required
# def index(request):

#     bks = Bikes.objects.all()
    
#     print(request.user.is_authenticated)

#     return render(request, 'index.html',{'bks':bks})

# class BikeDetail(DetailView):
#     model = Bikes
#     template_name = "rent.html"

def BikeDetail(request,slug_text):
    bk = Bikes.objects.filter(slug=slug_text)
    if bk.exists():
        bk=bk.first()
    else:
        return HttpResponse("<h1>Page not Found</h1>")
    context = {'bk':bk}
    return render(request,'rent.html',context)


def Index(request):
    # model = Bikes
    # template_name = 'index.html'
    bk = Bikes.objects.all()
    p = Paginator(bk, 3)
    page_num = request.GET.get('page', 1)
    page = p.page(page_num)
    context = {'items': page}
    return render(request,'index.html',context)


class rented(DetailView):
    model = Bikes
    template_name = 'rented.html'

def home(request):
    return render(request,'index.html')


def searchbar(request):
    return render(request,'searchbar.html')
    
        

def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        bk = Bikes.objects.all().filter(name__icontains=search)
        return render(request,'search.html',{'bk':bk})
    else:
        return render(request,'searchbar.html')

