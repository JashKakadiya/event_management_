from django.db import models
from django.core.validators import *
from django.utils import timezone
from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus
from django.core.exceptions import ValidationError
# from django.contrib.postgres.fields import ArrayField

class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_number = models.IntegerField()
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

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    # event_location_id = models.ForeignKey(EventLocation, on_delete=models.CASCADE)
    location_id = models.ForeignKey("EventLocation", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50,default='None')
    Event_from = models.DateTimeField()
    Event_to = models.DateTimeField()
    Image = models.ImageField(default='None', upload_to='static/uploads/images/')
    has_tickets = models.BooleanField(default=True)
    total_count = models.PositiveBigIntegerField(default=0)
    total_cost = models.PositiveBigIntegerField(default=0)
    total_price = models.PositiveBigIntegerField(default=0)
    # event_grand_total = models.PositiveBigIntegerField(null=True, blank=True,default=   0)
    paid_amount = models.PositiveBigIntegerField(default=0)
    pending_amount = models.PositiveBigIntegerField(default=0)
    has_sub_events = models.CharField(default='Yes', choices=(('Yes', 'Yes'), ('No', 'No')), max_length=3)

    created_on = models.DateTimeField(default = timezone.now)
    updated_on = models.DateTimeField(default = timezone.now,
                                    null = True, 
                                    blank = True
                                    )
    def __str__(self):
        return self.name

class EventLocation(models.Model):
    # event_location_id = models.IntegerField(primary_key=True)
    location_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    # event_id = models.IntegerField()
    title = models.CharField(max_length=50,default='None')
    address = models.CharField(max_length=250,default='None')
    street_detail = models.CharField(max_length=50,default='None')
    city = models.CharField(max_length=50, default='None')
    state = models.CharField(max_length=50,default='None')
    country = models.CharField(max_length=50,default='India')
    zipcode = models.IntegerField(default=0)
    location_link = models.CharField(max_length=200,default='None')
    def __str__(self):
        return self.title

class Subloca(models.Model):
    address = models.CharField(max_length=250)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return self.address

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

class Tickets(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=50, choices=( ('VIP', 'VIP'), ('BASE', 'BASE') ))
    ticket_price = models.IntegerField()
    ticket_count = models.IntegerField()
    ticket_description = models.CharField(max_length=50)
    created_on = models.DateTimeField(default = timezone.now)
    updated_on = models.DateTimeField(default = timezone.now,
                                    null = True, 
                                    blank = True
                                    )
    def __str__(self):
        return f"{self.event_id}--{self.ticket_type}--{self.ticket_count} "
    
class Order(models.Model):
    location_link = models.CharField(max_length=200,default='None')
    event_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    payment_event_id = models.IntegerField(default=0, null=False, blank=False)
    amount = models.FloatField(_("Amount"), null=True, blank=True)
    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )
    email = models.CharField(_("Email"), default='demo@abc.com' , max_length=128, null=False, blank=False)

    user_phone = models.IntegerField(_("Phone"), null=False, blank=False)
    
    event_name = models.CharField(_("Event Name"), max_length=128, null=False, blank=False)

    event_From = models.CharField(_("Event Date"), max_length=128, null=False, blank=False)

    ticket_type = models.CharField(_("Ticket Type"), max_length=128, null=True, blank=True)

    ticket_count = models.IntegerField(_("Ticket Count"), null=False, blank=False)

    ticket_used = models.CharField(_("Ticket Used"),default="No", max_length=128, null=True, blank=True)

    save_hash = models.CharField(_("Save Hash"), max_length=255, null=True, blank=True)

    save_url = models.CharField(_("Save URL"), max_length=255, null=True, blank=True)

    created_on = models.DateTimeField(default = timezone.now)
    updated_on = models.DateTimeField(default = timezone.now,
                                    null = True,
                                    blank = True
                                    )
    email_sent = models.BooleanField(default=False)
   
    def __str__(self):
        return f"{self.payment_id}--{self.save_hash}"
    
class Seats(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    seat_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    seat_count = models.IntegerField()
    created_on = models.DateTimeField(default = timezone.now)
    updated_on = models.DateTimeField(default = timezone.now,
                                    null = True, 
                                    blank = True
                                    )
    def __str__(self):
        return self.seat_name
    

class SystemConfigs(models.Model):
    system_config_DATABASE_USER = models.CharField(max_length=50)
    system_config_DATABASE_PASSWORD = models.CharField(max_length=50)
    system_config_RAZOR_KEY_ID = models.CharField(max_length=50)
    system_config_RAZOR_KEY_SECRET = models.CharField(max_length=50)
    system_config_PAYMENT_METHOD = models.CharField(max_length=50 , choices=( 
        ('RAZORPAY', 'RAZORPAY'), 
        ('PAYTM', 'PAYTM'),
        ('PAYPAL', 'PAYPAL'),
        ('CASH', 'CASH'), 
        ))
    system_config_EMAIL_HOST_USER = models.CharField(max_length=50)
    system_config_EMAIL_HOST_PASSWORD = models.CharField(max_length=50)
    system_config_COMPANY_TITLE = models.CharField(max_length=50)
    system_config_COMPANY_ADDRESS = models.CharField(max_length=50)
    system_config_COMPANY_PHONE = models.CharField(max_length=50)   
    system_config_COMPANY_EMAIL = models.CharField(max_length=50)
    system_config_COMPANY_LOGO = models.ImageField(upload_to='static/logo/', default='https://bootstrapious.com/i/snippets/sn-nav-logo/logo.png')
    system_config_Currency = models.CharField(max_length=50, default='INR')
    system_config_HOST_WEBSITE = models.CharField(max_length=250,default='http://127.0.0.1:8000/')
    system_config_COMPANY_LANDLINE = models.CharField(max_length=50)
    created_on = models.DateTimeField(default = timezone.now)
    updated_on = models.DateTimeField(default = timezone.now,
                                    null = True,
                                    blank = True
                                    )
    
    def save(self, *args, **kwargs):
        if not self.pk and SystemConfigs.objects.exists():
            raise ValidationError('There is can be only one SystemConfig instance')
        return super(SystemConfigs, self).save(*args, **kwargs)
    









# 1fed5f270af53e583158f231bfbf0e2480cd32e870dcab4ccda3bad1bfa0d598

    # config_id = models.AutoField(primary_key=True)
    # config_key = models.CharField(max_length=255 , choices=(
    #     ('system_config_DATABASE_NAME', 'DATABASE_NAME'),
    #     ('system_config_DATABASE_USER', 'DATABASE_USER'),
    #     ('system_config_DATABASE_PASSWORD', 'DATABASE_PASSWORD'),
    #     ('system_config_RAZOR_KEY_ID', 'RAZOR_KEY_ID'),
    #     ('system_config_RAZOR_KEY_SECRET', 'RAZOR_KEY_SECRET'),
    #     ('system_config_EMAIL_HOST_USER', 'EMAIL_HOST_USER'),
    #     ('system_config_RAZOR_KEY_SECRET', 'RAZOR_KEY_SECRET'),
    #     ('system_config_EMAIL_HOST_PASSWORD', 'EMAIL_HOST_PASSWORD'),
    #     ('system_config_PAYMENT_METHOD', 'PAYMENT_METHOD'),
    #     ('system_config_COMPANY_TITLE', 'COMPANY_TITLE'),
    #     ('system_config_COMPANY_LOGO', 'COMPANY_LOGO'),
    # ))
    # config_value = models.CharField(max_length=255)
    # created_on = models.DateTimeField(default = timezone.now)
    # updated_on = models.DateTimeField(default = timezone.now,
    #                                 null = True, 
    #                                 blank = True
    #                                 )
    # def __str__(self):
    #     return self.config_key


