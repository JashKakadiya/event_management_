from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_number = models.IntegerField()
    role = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    profile = models.CharField(max_length=50)
    status = models.BooleanField()
    deleted = models.CharField(max_length=50)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='None')
    parent_category = models.IntegerField()
    path = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    status = models.BooleanField()
    deleted = models.BooleanField()

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    email = models.EmailField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

class EventLocation(models.Model):
    event_location_id = models.AutoField(primary_key=True)
    event_id = models.IntegerField()
    title = models.CharField(max_length=50)
    street_detail = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    location_link = models.CharField(max_length=200)

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_parent_id = models.IntegerField()
    event_location_id = models.ForeignKey(EventLocation, on_delete=models.CASCADE)
    client_id = models.IntegerField()
    name = models.CharField(max_length=50)
    dateTime_from = models.DateTimeField()
    dateTime_to = models.DateTimeField()
    sub_events = models.ImageField()
    has_tickets = models.BooleanField()
    total_count = models.IntegerField()
    total_cost = models.IntegerField()
    total_price = models.IntegerField()
    event_grand_total = models.IntegerField()
    paid_amount = models.IntegerField()
    pending_amount = models.IntegerField()

class EventTransaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    transaction_number = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    amount = models.IntegerField()
    created_date = models.DateTimeField()

class EventCategory(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    catgory_id = models.ForeignKey(Category, on_delete=models.CASCADE)

class EventEmployee(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role_note = models.CharField(max_length=50)



