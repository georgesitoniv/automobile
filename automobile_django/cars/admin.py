from django.contrib import admin

from .models import Car, Color

class CarAdmin(admin.ModelAdmin):
    readonly_fields = ("slot_number", )

admin.site.register(Car, CarAdmin)
admin.site.register(Color)
