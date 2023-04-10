import mimetypes
from django.views import generic
from django.shortcuts import redirect, render
from .models import *
from django.http import JsonResponse
from django.http import HttpResponse
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from localStoragePy import localStoragePy
import json
from django.core.mail import send_mail, EmailMessage
from static.pypdf import test
import os
import random
import string
from .systemconfig import *
from qrcode import *
from .qrcoded import *
import smtplib
from urllib.parse import urlparse,parse_qs 
from .fusioncharts import FusionCharts
from wsgiref.util import FileWrapper
import time


razorpay_client = razorpay.Client(
    auth=(get_razor_key_id(), get_razor_key_secret()))


def TicketsView(request):
    context = {
        'id': id
    }
    return render(request, 'frontend/tickets.html')


@csrf_exempt
def PaymentView(request):
    start = time.time()

    def verify_signature(response_data):
        client = razorpay.Client(
            auth=(get_razor_key_id(), get_razor_key_secret()))
        return client.utility.verify_payment_signature(response_data)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()
        if order.ticket_type == 'BASE':
            ticket = Tickets.objects.filter(event_id=order.event_id).order_by('ticket_type')[0]
            event_ticket_remaining = Tickets.objects.filter(event_id=order.event_id).values('ticket_count').order_by("ticket_type")[0]['ticket_count']
            ticket.ticket_count = event_ticket_remaining - order.ticket_count
        elif order.ticket_type == 'VIP':
            ticket = Tickets.objects.filter(event_id=order.event_id).order_by('ticket_type')[1]
            event_ticket_remaining = Tickets.objects.filter(event_id=order.event_id).values('ticket_count').order_by("ticket_type")[1]['ticket_count']
            ticket.ticket_count = event_ticket_remaining - order.ticket_count

        ticket.save()
        # tickets.ticket_count = event_ticket_remaining[0]['ticket_count'] - 1
        print(order)
        if verify_signature({
            "razorpay_payment_id": payment_id,
            "razorpay_order_id": provider_order_id,
            "razorpay_signature": signature_id,
        }):
            order.status = PaymentStatus.SUCCESS
            event_location = EventLocation.objects.get(location_id=order.event_id)
            event = Event.objects.get(event_id=order.event_id)
            event.total_count -= order.ticket_count
            print("............",event.total_count,order.ticket_count)
            event.save()
            order.location_link = event_location.location_link
            order.save()
            temp_hash= generate_hash(order)
            temp_generate_url = generate_url(temp_hash)
            invoive_qrcode(temp_generate_url,order)
            order.save_hash = temp_hash
            order.save_url = temp_generate_url
            order.save()
            print(order)
            cvt_start = time.time()
            test.convert_to_pdf(order,get_host_companyName(request),event_location,event)
            cvt_end = time.time()
            print("eonverter",cvt_end-cvt_start)

            mail_start = time.time()
            Mail_send(order,str(get_host_email()),order.email,str(get_host_password()))
            mail_end = time.time()
            print("mail",mail_end-mail_start)
            end = time.time()
            print("full function",end - start)
            return render(request, "frontend/sucess.html", context={"status": order.status})
            
            
        else:
            order.status = PaymentStatus.FAILURE
            order.save()
            return render(request, "frontend/fauiler.html", context={"status": order.status})
    else:
        if request.POST.get("error[metadata]"):
            payment_id = json.loads(request.POST.get(
            "error[metadata]")).get("payment_id")
            provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
                "order_id"
            )
            order = Order.objects.get(provider_order_id=provider_order_id)
            order.payment_id = payment_id
            order.status = PaymentStatus.FAILURE
            order.save()
            return render(request, "frontend/payment.html", context={"status": order.status})
        else:
            return render(request, "frontend/sucess.html")

    # if request.method == "POST":
    #     try:

    #         # get the required parameters from post request.
    #         payment_id = request.POST.get('razorpay_payment_id', '')
    #         razorpay_order_id = request.POST.get('razorpay_order_id', '')
    #         signature = request.POST.get('razorpay_signature', '')
    #         params_dict = {
    #             'razorpay_order_id': razorpay_order_id,
    #             'razorpay_payment_id': payment_id,
    #             'razorpay_signature': signature
    #         }

    #         # verify the payment signature.
    #         result = razorpay_client.utility.verify_payment_signature(
    #             params_dict)
    #         print(",,,,,,,,,,,,,,,",result)
    #         if result is not None:
    #             amount = 2000 # Rs. 200
    #             try:
    #                 # capture the payemt
    #                 razorpay_client.payment.capture(payment_id, amount)

    #                 # render success page on successful caputre of payment
    #                 return render(request, 'paymentsuccess.html')
    #             except:

    #                 # if there is an error while capturing payment.
    #                 return render(request, 'paymentfail.html')
    #         else:

    #             # if signature verification fails.
    #             return render(request, 'paymentfail.html')
    #     except:

    #         # if we don't find the required parameters in POST data
    #         return HttpResponseBadRequest()
    # else:
    #    # if other than POST request is made.
    #     return HttpResponseBadRequest()


def IndexView(request):
    event_location = EventLocation.objects.all()
    event_item = Event.objects.all()
    context = {
        'event_location': event_location,
        'event_item': event_item,
        'today': datetime.now(),
    }
    return render(request, 'frontend/index.html', context)


def popup_data(request, id):
    event_location = EventLocation.objects.all()
    event_item = Event.objects.all()
    tickets_item = Tickets.objects.filter(event_id=id)
    context = {
        'event_location': list(event_location.values()),
        'event_item': list(event_item.values()),
        'tickets_item': list(tickets_item.values().order_by('ticket_type')),
    }
    return JsonResponse(context)


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

@csrf_exempt
def Razorpay(request):
    event_name = request.POST.get('event_name')
    ticket_count = request.POST.get('ticket_count')
    ticket_type = request.POST.get('ticket_type')
    payment_event_id = request.POST.get('event_id')
    amount = int(request.POST.get('total'))
    user_email = request.POST.get('email')
    user_phone = request.POST.get('phone')
    user_name = request.POST.get('user_name')
    event_id = request.POST.get('event_id')
    event_From = Event.objects.get(event_id=payment_event_id)
    event_From = event_From.Event_from.strftime('%Y-%m-%d %H:%M:%S')

    order_currency = 'INR'
    razorpay_order = razorpay_client.order.create(dict(amount=amount*100,
                                                       currency=order_currency,
                                                       payment_capture='0'))

    order = Order.objects.create(
        user_name=user_name,
        event_id=event_id,
        event_name=event_name,
        ticket_count=ticket_count,
        ticket_type=ticket_type,
        event_From=event_From,
        amount=amount,
        provider_order_id=razorpay_order['id'],
        email=user_email,
        user_phone=user_phone,
        payment_event_id=payment_event_id
    )
    order.save()
    razorpay_order_id = razorpay_order['id']
    callback_url = "/razorpay/payment/"
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = get_razor_key_id()
    context['razorpay_amount'] = amount
    context['currency'] = order_currency
    context['callback_url'] = callback_url
    # context['order'] = order

    return JsonResponse(context)


def freepay(request):
    event_name = request.POST.get('event_name')
    ticket_count = request.POST.get('ticket_count')
    ticket_type = request.POST.get('ticket_type')
    user_name = request.POST.get('user_name')
    event_id = request.POST.get('event_id')
    payment_event_id = request.POST.get('event_id')
    user_email = request.POST.get('email')
    user_phone = request.POST.get('phone')
    event_From = Event.objects.get(event_id=payment_event_id)
    event_From = event_From.Event_from.strftime('%Y-%m-%d %H:%M:%S')
    # random generate 16 character ticket
    ticket = ''.join(random.choices(
        string.ascii_uppercase + string.ascii_lowercase, k=16))
    
    order = Order.objects.create(
        user_name=user_name,
        event_id=event_id,
        event_name=event_name,
        ticket_count=ticket_count,
        ticket_type='Base',
        event_From=event_From,
        amount=0,
        provider_order_id=ticket,
        email=user_email,
        user_phone=user_phone,
        payment_event_id=payment_event_id,
        status='success',
        payment_id=ticket


    )
    event_location = EventLocation.objects.get(location_id=order.event_id)
    order.location_link = event_location.location_link
    temp_hash= generate_hash(order)
    temp_generate_url = generate_url(temp_hash)
    invoive_qrcode(temp_generate_url,order)
    order.save_hash = temp_hash
    order.save_url = temp_generate_url
    order.save()
    
    event = Event.objects.get(event_id=order.event_id)
    test.convert_to_pdf(order,get_host_companyName(request),event_location,event)
    Mail_send(order,str(get_host_email()),order.email,str(get_host_password()))
    
#     subject = 'Event Management Payment'
#     message = f'''Hi {order.user_name}, thank you for registering in Event.

# your order is successfully placed.
            
# order id: {order.provider_order_id}      
# order amount: {int(order.amount)}/- rupees only
# order status: {order.status}
# Phone number: {order.user_phone}
                            
                            
                            
#                             '''
#     email_from = get_host_email()
#     recipient_list = [order.email]
#     email = EmailMessage(subject, message, email_from, recipient_list)
#     fd = open("invoice.pdf", 'rb')
#     email.attach("invoice.pdf", fd.read(), 'application/pdf')
#     email.send()

    return JsonResponse({'status': 'success'})


def success(request):
    return render(request, 'frontend/sucess.html')

@csrf_exempt
def customer_view(request):
   
    url = request.build_absolute_uri()

    query_params = urlparse(url).query
    params_dict = dict(parse_qs(query_params))

    data = params_dict.get('data')


    if request.method == "POST":
        data = json.loads(request.POST.get('data')) 
        print(",,,,,,,,,,,,,,,,,,,,,,",data)
        try:
            ticket = Order.objects.get(payment_id=data['id'])
            print(ticket)

            if ticket:
                ticket.ticket_used = 'Yes'
                ticket.save()
                return HttpResponse("True")
        except:
            return HttpResponse("Error")


    if data:
        
        try:
            print("try",data[0])
            ticket = Order.objects.get(save_hash=data[0])
            if ticket:
                context = {
                    "ticket_sale": ticket,
                }
                return render(request,'frontend/ticket_view.html',context)
        except:    
            return render(request,'frontend/ticket_fail_view.html')
    return HttpResponse(str(request.build_absolute_uri()))

# The `chart` function is defined to generate Column 2D chart from database.
def analysis_view(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Total Sales of each Event",
            "subCaption": "",
            "xAxisName": "Events",
            "yAxisName": "Ticket remaining",
            "numberPrefix": "Ps. ",
            "theme": "fusion"
        }

    # The data for the chart should be in an array where each element of the array is a JSON object
    # having the `label` and `value` as key value pair.

    dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in Event.objects.all():
      data = {}
      data['label'] = key.name
      data['value'] = key.total_count
      dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor
    column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-1", "json", dataSource)
    return render(request, 'frontend/analysis.html', {'output': column2D.render()})

def sysconfigs():
    return redirect('/admin/event_management_application/systemconfigs/1/change/')

def redeemed(request):
    return render(request,'frontend/redeemed.html')

@csrf_exempt
def contact_us(request):
    email = request.POST.get('contact_email')
    name = request.POST.get('contact_name')
    phone= request.POST.get('contact_phone')
    message = request.POST.get('contact_subject') + request.POST.get('contact_message') 
    subject = " Email from "+ email + " Name: "+ name + " Phone: "+ phone
    send_mail(subject, message, email, [get_host_email()], fail_silently=False)
    return JsonResponse({'status': 'success'})



# Define function to download pdf file using template
def download_pdf_file(request):
    filename = 'invoice.pdf'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + '/' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

