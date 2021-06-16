from django.urls import path

from . import views

urlpatterns = [
    path('',views.Index,name='index'),
    path('searchbar/',views.searchbar,name='searchbar'),
    path('search/',views.search,name='search'),
    path('rent/<slug:slug_text>',views.BikeDetail,name = 'rent'),
    path('rented/<int:pk>',views.rented.as_view(),name='rented'),
    
    #path('list-test/', views.BikesListView.as_view())
]
