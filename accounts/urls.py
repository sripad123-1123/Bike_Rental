from django.urls import path
from django.urls.conf import include


from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('token_send',views.token_send,name='token_send'),
    path('success/',views.success,name='success'),
    path('verify/<token>',views.verify,name = 'verify')

    
]

