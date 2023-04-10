from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.shortcuts import render

from .models import *


class EventlocationInline(admin.StackedInline):
    model = EventLocation
    extra = 1


class SubloationInline(admin.StackedInline):
    model = Subloca
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = [EventlocationInline, SubloationInline]

    list_display = ('name', 'Event_from', 'Event_to', 'Image', 'has_tickets', 'total_count',
                    'total_cost', 'total_price', 'paid_amount', 'pending_amount', 'has_sub_events')
    exclude = ('created_on', 'updated_on')
    change_form_template = "admin/custom_change_form.html"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        location = EventLocation.objects.last().location_id

        event = Event.objects.get(event_id=Event.objects.last().event_id)
        event.location_id = EventLocation.objects.get(location_id=location)
        event.save()

    def edit_button(self, obj):
        url = reverse('admin:events_event_change', args=[obj.id])
        return format_html('<a class="button" href="{}">Edit</a>', url)
    edit_button.short_description = 'Edit Event'


class EventLocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'street_detail', 'city',
                    'state', 'country', 'zipcode', 'location_link')


class TicketAdmin(admin.ModelAdmin):
    list_display=('ticket_id','event_id','ticket_type','ticket_price','ticket_count','ticket_description','created_on','updated_on')
    exclude = ('created_on', 'updated_on')


admin.site.register(Event, EventAdmin)
admin.site.register(EventLocation, EventLocationAdmin)
admin.site.register(Subloca)
admin.site.register(Employee)
admin.site.register(Tickets, TicketAdmin)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'payment_event_id', 'amount', 'status', 'payment_id', 'ticket_count', 'ticket_used', 'updated_on')

# class SystemConfigAdmin(admin.ModelAdmin):

#     add_form_template = 'admin/systemconfig/ten_configs.html'
#     def get_urls(self):
#         from django.urls import path
#         urls = super().get_urls()
#         custom_urls = [
#             path('ten_configs/', self.admin_site.admin_view(self.ten_configs_view)),
#         ]
#         return custom_urls + urls

#     def ten_configs_view(self, request):
#         config_list = SystemConfig.objects.order_by('config_key')[:5]
#         return admin.site.admin_view(
#             lambda req: self.display_configs(config_list, req)
#         )(request)

#     def display_configs(self, config_list, request):
#         context = {
#             'config_list': config_list,

#         }
#         return render(request, 'admin/systemconfig/ten_configs.html', context)


@admin.register(SystemConfigs)
class SystemConfigsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Company details", {
            'fields': ('system_config_COMPANY_TITLE', 'system_config_COMPANY_EMAIL', 'system_config_COMPANY_PHONE', 'system_config_COMPANY_ADDRESS','system_config_COMPANY_LOGO','system_config_COMPANY_LANDLINE','system_config_HOST_WEBSITE')
        }),
        ("Email", {
            'fields': ('system_config_EMAIL_HOST_USER', 'system_config_EMAIL_HOST_PASSWORD')
        }),
        ("Database", {
            'fields': ('system_config_DATABASE_USER', 'system_config_DATABASE_PASSWORD')
        }),
        ("Payment details", {
            'fields': ('system_config_PAYMENT_METHOD', 'system_config_RAZOR_KEY_ID', 'system_config_RAZOR_KEY_SECRET','system_config_Currency')
        }),
    )
    list_display = ('system_config_COMPANY_TITLE', 'system_config_COMPANY_EMAIL', 'system_config_COMPANY_PHONE', 'system_config_COMPANY_ADDRESS','system_config_COMPANY_LOGO','system_config_EMAIL_HOST_USER', 'system_config_EMAIL_HOST_PASSWORD','system_config_PAYMENT_METHOD', 'system_config_RAZOR_KEY_ID', 'system_config_RAZOR_KEY_SECRET','system_config_Currency','system_config_DATABASE_USER', 'system_config_DATABASE_PASSWORD')
    exclude = ('created_on', 'updated_on')
