from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Employee)
admin.site.register(Category)
admin.site.register(Client)
admin.site.register(EventLocation)
admin.site.register(Event)
admin.site.register(EventTransaction)
admin.site.register(EventCategory)
admin.site.register(EventEmployee)
