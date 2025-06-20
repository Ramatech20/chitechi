from django.contrib import admin
from .models import Participant

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'user', 'registration_date', 'status')
    search_fields = ('name', 'phone_number', 'user__username')
    list_filter = ('status',)
    exclude = ('event',)

# Register your models here.
