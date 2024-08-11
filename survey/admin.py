from django.contrib import admin
from .models import EmojiFeedback


# Register your models here.

@admin.register(EmojiFeedback)
class EmojiFeedbackAdmin(admin.ModelAdmin):
    list_display = ('emoji', 'count')
