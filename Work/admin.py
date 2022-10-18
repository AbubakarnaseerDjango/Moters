from django.contrib import admin
from . models import Contact,Product,CustomerServices,Catagry
# Register your models here.

admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(CustomerServices)
admin.site.register(Catagry)