from django.contrib import admin
from .models import Order, OrderItem


class OrderInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'created', 'updated', 'paid', 'display_name', 'city']
    fields = (('first_name', 'last_name'), 'email', ('address', 'postal_code', 'city'), 'paid')
    inlines = [OrderInline]
    list_filter = ['paid']
