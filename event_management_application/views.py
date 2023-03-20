from django.views import generic

class IndexView(generic.ListView):
    template_name = 'employee/employee.html'
    def get_queryset(self):
        return None
    
class EmployeeView(generic.ListView):
    template_name = 'employee/employee.html'
    def get_queryset(self):
        return None
    
class CatagoryView(generic.ListView):
    template_name = 'event_catagory/catagory.html'
    def get_queryset(self):
        return None

class EventView(generic.ListView):
    template_name = 'event/event.html'
    def get_queryset(self):
        return None
    
class Eventlocation(generic.ListView):
    template_name = 'event_location/event_location.html'
    def get_queryset(self):
        return None
    
class Eventransaction(generic.ListView):
    template_name = 'transactions/transactions.html'
    def get_queryset(self):
        return None
    
class ClientView(generic.ListView):
    template_name = 'client/client.html'
    def get_queryset(self):
        return None
    
class EmployeeDashboardView(generic.ListView):
    template_name = 'employee/employee_dashboard.html'
    def get_queryset(self):
        return None
    
class ClientDashboardView(generic.ListView):
    template_name = 'client/client_dashboard.html'
    def get_queryset(self):
        return None
    
class TransactionsDashboardView(generic.ListView):
    template_name = 'transactions/transactions_dashboard.html'
    def get_queryset(self):
        return None
    
class EventDashboardView(generic.ListView):
    template_name = 'event/event_dashboard.html'
    def get_queryset(self):
        return None
    
class EventCatagoryView(generic.ListView):
    template_name = 'event_catagory/catagory_dashboard.html'
    def get_queryset(self):
        return None