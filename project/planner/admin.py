from django.contrib import admin

from .models import Plan, Event

# Register your models here.

admin.site.register(Plan)
admin.site.register(Event)