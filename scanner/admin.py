from django.contrib import admin
from .models import QRCode

@admin.register(QRCode)
class QRAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'mobile_number']