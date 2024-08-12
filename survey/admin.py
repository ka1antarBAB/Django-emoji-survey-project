from django.contrib import admin
from .models import Survey


# Register your models here.

@admin.register(Survey)
class EmojiFeedbackAdmin(admin.ModelAdmin):
    list_display = ('emoji', 'count')
