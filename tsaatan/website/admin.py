from django.contrib import admin
from .models import *
# Register your models here.


class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'sale')
    # list_filter = ('filter')
    # list_editable = ('sale')
    # list_display_links = ('name')


admin.site.register(Product, productAdmin)
admin.site.register(Category)
admin.site.register(SliderPicture)
admin.site.register(Vaucher)
admin.site.register(Address)
admin.site.register(About)
