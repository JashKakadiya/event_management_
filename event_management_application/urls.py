from django.urls import path
from . import views
from django.views.generic import RedirectView 


urlpatterns = [
   
    path('', views.IndexView, name='index'),
    path('payment/', views.PaymentView, name='payment'),
    path('razorpay/', views.Razorpay, name='paymentstatus'),
    path('freepay/', views.freepay, name='freepay'),
    path('success/', views.success, name='success'),
    path('contact_us/', views.contact_us, name='contact_us'),
    # path('employee/', views.EmployeeView.as_view(), name='employee'),
    # path('catagory/', views.CatagoryView.as_view(), name='catagory'),
    # path('event/', views.EventView.as_view(), name='event'),
    # path('event_location/', views.Eventlocation.as_view(), name='event_location'),
    # path('transactions/', views.Eventransaction.as_view(), name='transactions'),
    # path('client/', views.ClientView.as_view(), name='client'),
    # path('employee_dashboard/', views.EmployeeDashboardView.as_view(), name='employee_dashboard'),
    # path('client_dashboard/', views.ClientDashboardView.as_view(), name='client_dashboard'),
    # path('transactions_dashboard/', views.TransactionsDashboardView.as_view(), name='transactions_dashboard'),
    # path('event_dashboard/', views.EventDashboardView.as_view(), name='event_dashboard'),
    # path('catagory_dashboard/', views.EventCatagoryView.as_view(), name='catagory_dashboard'),
    path('popup_data/<int:id>', views.popup_data, name='popup_data'),
    path('tickets/', views.TicketsView, name='tickets'),
    path('customer/', views.customer_view, name='customer'),
    path('analysis/', views.analysis_view, name='analysis'),
    path('redeemed/', views.redeemed, name='redeemed'),
    path('downloadpdf/', views.download_pdf_file, name='downloadpdf'),
    path('event_detail/', views.event_detail, name='event_detail'),

]
