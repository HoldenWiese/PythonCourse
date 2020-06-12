from django.contrib import admin

# Register your models here.
from .models import UserAccount
from .models import UserTransaction

admin.site.register(UserAccount)
admin.site.register(UserTransaction)