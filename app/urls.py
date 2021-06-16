from django.urls import path

from . import views

urlpatterns = [
    
    path('rent/',views.rent,name='rent'),
    path('rented/<str:pk1>/',views.rented,name='rented'),
    path('history/',views.history,name = 'history')
]

