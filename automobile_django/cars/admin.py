from django.contrib import admin

from .models import Car, Color

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'order' )
    list_filter = ('color', )
    search_fields = ['name', 'color__name', ]
    fields = ('order', 'name', 'color',)
    readonly_fields = ('order', )

admin.site.register(Car, CarAdmin)
admin.site.register(Color)
