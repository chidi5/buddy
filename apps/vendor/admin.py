from django.contrib import admin
from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(Vendor, VendorAdmin)
