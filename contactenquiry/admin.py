from django.contrib import admin
from contactenquiry.models import contacteEnquiry
# Register your models here.
class contactenquiryadmin(admin.ModelAdmin):
    list_display=('name','email','phone','message')

admin.site.register(contacteEnquiry,contactenquiryadmin)