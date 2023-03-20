from django.contrib import admin

# Register your models here.
from .models import *
  
class StateAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'is_active', 'created_on')
  
    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True
  
admin.site.register(Employee, StateAdmin)

# admin.site.register(Employee)
admin.site.register(Category)
admin.site.register(Client)
admin.site.register(EventLocation)
admin.site.register(Event)
admin.site.register(EventTransaction)
admin.site.register(EventCategory)
admin.site.register(EventEmployee)
