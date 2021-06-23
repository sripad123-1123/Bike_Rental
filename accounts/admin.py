from django.contrib import admin
from . models import Account, profile_verify

# Register your models here.
admin.site.register(Account)
admin.site.register(profile_verify)