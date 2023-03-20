from django.db import models
from django.core.validators import *
from django.utils import timezone


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True,validators=[MinValueValidator(6)])
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_number = models.IntegerField()
    role = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_number = models.IntegerField(validators=[MaxLengthValidator(10)])
    email = models.CharField(max_length=50)
    profile = models.CharField(max_length=50)
    is_active = models.IntegerField(default = 1,
                                   blank = True,
                                    null = True,
                                    help_text ='1->Active, 0->Inactive', 
                                    choices =(
                                    (1, 'Active'), (0, 'Inactive')
                                    ))
    deleted = models.IntegerField(default = 0,
                                   blank = True,
                                    null = True,
                                    help_text ='1->yes, 0->No', 
                                    choices =(
                                    (1, 'yes'), (0, 'No')
                                    ))
    created_on = models.DateTimeField(default = timezone.now)
    updated_on = models.DateTimeField(default = timezone.now,
                                    null = True, 
                                    blank = True
                                    )
    def __str__(self):
        return self.first_name

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='None')
    parent_category = models.IntegerField()
    path = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    is_active = models.IntegerField(default = 1,
                                   blank = True,
                                    null = True,
                                    help_text ='1->Active, 0->Inactive', 
                                    choices =(
                                    (1, 'Active'), (0, 'Inactive')
                                    ))
    deleted = models.IntegerField(default = 0,
                                   blank = True,
                                    null = True,
                                    help_text ='1->yes, 0->No', 
                                    choices =(
                                    (1, 'yes'), (0, 'No')
                                    ))
    def __str__(self):
        return self.name

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=50)
    contact_number = models.IntegerField(validators=[MaxLengthValidator(10)])
    email = models.EmailField()
    created_on = models.DateTimeField(default = timezone.now)
    updated_on = models.DateTimeField(default = timezone.now,
                                    null = True, 
                                    blank = True
                                    )
    def __str__(self):
        return self.client_name

class EventLocation(models.Model):
    event_location_id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    title = models.CharField(max_length=50)
    street_detail = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.IntegerField(validators=[MaxLengthValidator(6)])
    location_link = models.CharField(max_length=200)
    def __str__(self):
        return self.title

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
    created_on = models.DateTimeField(default = timezone.now)
    updated_on = models.DateTimeField(default = timezone.now,
                                    null = True, 
                                    blank = True
                                    )
    def __str__(self):
        return self.name

class EventTransaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    transaction_number = models.IntegerField()
    payment_method = models.CharField(max_length=50,choices=( ('Cash', 'Cash'), ('Cheque', 'Cheque'), ('Online', 'Online'), ('Other', 'Other') ))
    amount = models.IntegerField()
    created_on = models.DateTimeField(default = timezone.now)
    updated_on = models.DateTimeField(default = timezone.now,
                                    null = True, 
                                    blank = True
                                    )
    def __str__(self):
        return self.amount

class EventCategory(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    catgory_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.event_id

class EventEmployee(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role_note = models.CharField(max_length=50)
    def __str__(self):
        return self.event_id



