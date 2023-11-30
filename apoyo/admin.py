from django.contrib import admin
from .models import Donacion, AddPatient
# Register your models here.

class DonacionAdmin(admin.ModelAdmin):
    readonly_fields = ("Fecha", )

admin.site.register(Donacion, DonacionAdmin )
admin.site.register(AddPatient)