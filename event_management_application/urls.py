from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('employee/', views.EmployeeView.as_view(), name='employee'),
    path('catagory/', views.CatagoryView.as_view(), name='catagory'),
    path('event/', views.EventView.as_view(), name='event'),
    path('event_location/', views.Eventlocation.as_view(), name='event_location'),
    path('transactions/', views.Eventransaction.as_view(), name='transactions'),
    path('client/', views.ClientView.as_view(), name='client'),
    path('employee_dashboard/', views.EmployeeDashboardView.as_view(), name='employee_dashboard'),
    path('client_dashboard/', views.ClientDashboardView.as_view(), name='client_dashboard'),
    path('transactions_dashboard/', views.TransactionsDashboardView.as_view(), name='transactions_dashboard'),
    path('event_dashboard/', views.EventDashboardView.as_view(), name='event_dashboard'),
    path('catagory_dashboard/', views.EventCatagoryView.as_view(), name='catagory_dashboard'),
]
