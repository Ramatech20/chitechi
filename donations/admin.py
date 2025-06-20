from django.contrib import admin
from .models import Donation, Payment

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'created_at')
    search_fields = ('user__username',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'method', 'status', 'created_at')
    search_fields = ('user__username', 'transaction_id')
