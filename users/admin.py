from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address', 'location')
    search_fields = ('user__username', 'phone_number', 'location')
    list_filter = ('location',)