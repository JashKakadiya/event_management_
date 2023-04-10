from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from django.urls import reverse_lazy
admin.site.site_header = "Event Management Admin"
urlpatterns = [
     path('admin/event_management_application/systemconfigs/', RedirectView.as_view(url='/admin/event_management_application/systemconfigs/1/change/', permanent=False), name='sysconfig'),  
    path("admin/", admin.site.urls),
    path("",include("event_management_application.urls")),

    # path('admin/event_management_application/systemconfigs/', include("event_management_application.urls")),
    path("payment/",include("event_management_application.urls")),
    path("razorpay/",include("event_management_application.urls")),
    path("freepay/",include("event_management_application.urls")),
    path("success/",include("event_management_application.urls")),
    path("contact_us/",include("event_management_application.urls")),
    # path("employee/",include("event_management_application.urls")),
    # path("catagory/",include("event_management_application.urls")),
    # path("event/",include("event_management_application.urls")),
    # path("event_location/",include("event_management_application.urls")),
    # path("transactions/",include("event_management_application.urls")),
    # path("client/",include("event_management_application.urls")),
    # path("employee_dashboard/",include("event_management_application.urls")),
    # path("client_dashboard/",include("event_management_application.urls")),
    # path("transactions_dashboard/",include("event_management_application.urls")),
    # path("event_dashboard/",include("event_management_application.urls")),
    # path("catagory_dashboard/",include("event_management_application.urls")),
    path("tickets/",include("event_management_application.urls")),
    path("popup_data/<int:id>",include("event_management_application.urls")),
    path("customer/",include("event_management_application.urls")),
    path("analysis/",include("event_management_application.urls")),
    path("redeemed/",include("event_management_application.urls")),
    path("downloadpdf/",include("event_management_application.urls")),
  


]
