from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'feedback_type', 'created_at', 'resolved')
    list_filter = ('feedback_type', 'resolved')
    search_fields = ('user__username', 'message')

# Register your models here.
