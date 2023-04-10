from django.core.mail import send_mail
from django_cron import CronJobBase, Schedule
from event_management_application.models import Order

class DailyEmail(CronJobBase):
    RUN_AT_TIMES = ['03:30']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'event_management_application.daily_email'

    def do(self):
        orders = Order.objects.filter(email_sent=False)
        emails = orders.values_list('email', flat=True)
        sent_count = send_mail('Daily Email', 'This is a daily email', 'from@example.com', emails, fail_silently=False)
        if sent_count > 0:
            orders.update(email_sent=True)
