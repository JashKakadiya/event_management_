from django.contrib import admin
from django.urls import path,include
admin.site.site_header = "Event Management Admin"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("event_management_application.urls")),
    path("employee/",include("event_management_application.urls")),
    path("catagory/",include("event_management_application.urls")),
    path("event/",include("event_management_application.urls")),
    path("event_location/",include("event_management_application.urls")),
    path("transactions/",include("event_management_application.urls")),
    path("client/",include("event_management_application.urls")),
    path("employee_dashboard/",include("event_management_application.urls")),
    path("client_dashboard/",include("event_management_application.urls")),
    path("transactions_dashboard/",include("event_management_application.urls")),
    path("event_dashboard/",include("event_management_application.urls")),
    path("catagory_dashboard/",include("event_management_application.urls")),


]
