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
    path('popup_data/<int:id>', views.popup_data, name='popup_data'),
    path('tickets/', views.TicketsView, name='tickets'),
    path('customer/', views.customer_view, name='customer'),
    path('analysis/', views.analysis_view, name='analysis'),
    path('redeemed/', views.redeemed, name='redeemed'),
    path('downloadpdf/', views.download_pdf_file, name='downloadpdf'),
    path('event_detail/', views.event_detail, name='event_detail'),
    path('recent_transactions/', views.recent_transactions, name='recent_transactions'),
    path('choices/', views.choices, name='choices'),

]
