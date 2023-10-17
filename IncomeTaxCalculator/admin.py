from django.contrib import admin
from .models import IncomeTaxDetails, CalculatedIncomeTax

# Register your models here.
admin.site.register(IncomeTaxDetails)
admin.site.register(CalculatedIncomeTax)