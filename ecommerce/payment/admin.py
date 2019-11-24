from django.contrib import admin

from ecommerce.payment.models import Payment


class ProductAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'phone_no', 'address', 'state',
                    'city', 'card_name', 'card_number', 'expiring_month', 'expiring_year', 'card_cvv')


admin.site.register(Payment, ProductAdmin)
