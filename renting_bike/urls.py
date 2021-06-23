from django.urls import path

from . import views

urlpatterns = [
    path('',views.Index,name='index'),
    path('bookings/',views.bookings,name = 'bookings'),
    path('searchbar/',views.searchbar,name='searchbar'),
    path('search/',views.search,name='search'),
    path('rent/<slug:slug_text>',views.BikeDetail,name = 'rent'),
   
    
   
]
