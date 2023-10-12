from .models import SystemConfigs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import time 

if SystemConfigs.objects.all().count() ==0:
    print("yes")
    SystemConfigs.objects.create()
else:
    pass

systemconfig_obj = SystemConfigs.objects.first()


def get_host_email():
    if systemconfig_obj.system_config_EMAIL_HOST_USER:

        return systemconfig_obj.system_config_EMAIL_HOST_USER
    else:
        return "example@email"

def get_host_password():
    if systemconfig_obj.system_config_EMAIL_HOST_PASSWORD:
        return systemconfig_obj.system_config_EMAIL_HOST_PASSWORD
    else:
        return "password"
    

def get_razor_key_id():
    if systemconfig_obj.system_config_RAZOR_KEY_ID:
        return systemconfig_obj.system_config_RAZOR_KEY_ID
    else:
        return "is"
    
def get_razor_key_secret():
    if systemconfig_obj.system_config_RAZOR_KEY_SECRET:

        return systemconfig_obj.system_config_RAZOR_KEY_SECRET
    else:
        return "key"

def get_host_companyName(request):
    if systemconfig_obj.system_config_COMPANY_TITLE:
        return {'company_name':systemconfig_obj.system_config_COMPANY_TITLE}
    else:
        return "C_name"

def get_host_companyAddress():
    if systemconfig_obj.system_config_COMPANY_ADDRESS:

        return systemconfig_obj.system_config_COMPANY_ADDRESS
    else:
        return "Address"

def get_host_companyPhone(request):
    if systemconfig_obj.system_config_COMPANY_PHONE:
    
        return {'company_Phone':systemconfig_obj.system_config_COMPANY_PHONE}

    else:
        return "0000"

def get_host_companyEmail():
    if systemconfig_obj.system_config_COMPANY_EMAIL:
        return systemconfig_obj.system_config_COMPANY_EMAIL
    else:
        return ""

def get_host_paymentMethod():
    if systemconfig_obj.system_config_PAYMENT_METHOD:

        return systemconfig_obj.system_config_PAYMENT_METHOD
    else:
        return ""

def get_host_databaseUserName():
    if systemconfig_obj.system_config_DATABASE_USER:
        return systemconfig_obj.system_config_DATABASE_USER
    
    else:
        return ""
    
def get_host_CompanyLogo(request):
    if systemconfig_obj.system_config_COMPANY_LOGO:
        return {'company_logo': systemconfig_obj.system_config_COMPANY_LOGO}
    else:
        return {'company_logo':"https://bootstrapious.com/i/snippets/sn-nav-logo/logo.png"}
    
def get_host_Currency(request):
    if systemconfig_obj.system_config_Currency:
        return {'payment_curruncy':systemconfig_obj.system_config_Currency}
    else:
        return ""


def get_host_companyAddress_html(request):
    if systemconfig_obj.system_config_COMPANY_ADDRESS:
        return {'company_address':systemconfig_obj.system_config_COMPANY_ADDRESS}
    else:
        return ""

def get_host_companyEmail_html(request):
    if systemconfig_obj.system_config_COMPANY_EMAIL:
        return {'company_email':systemconfig_obj.system_config_COMPANY_EMAIL}
    else:
        return ""
    

def get_host_companyLandline_html(request):
    if systemconfig_obj.system_config_COMPANY_LANDLINE:
        return {'company_landline':systemconfig_obj.system_config_COMPANY_LANDLINE}
    else:
        return ""

def get_host_website():
    if systemconfig_obj.system_config_HOST_WEBSITE:
        return systemconfig_obj.system_config_HOST_WEBSITE
    else:
        return "http://127.0.0.1:8000/"
    
def get_host_website_html(request):
    if systemconfig_obj.system_config_HOST_WEBSITE:
        return {'host_website':systemconfig_obj.system_config_HOST_WEBSITE}
    else:
        return ""

def Mail_send(data,email_from,email_to,email_password):
    start = time.time()
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] =  'Event Management Payment'
    body = f'''Hi {data.user_name}, thank you for registering in Event.

Your order is successfully placed.
            
Order id: {data.provider_order_id}      
Order amount: {int(data.amount)}/- rupees only
Order status: {data.status}
Phone number: {data.user_phone}   
                            '''
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(os.path.abspath(os.path.dirname('static/invoices/'))+f'/{data.payment_id}.pdf', "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % f'/{data.payment_id}.pdf')
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email_from, email_password)
    text = msg.as_string()
    s.sendmail(email_from,email_to, text)
    s.quit()
    end = time.time()
    print("mail_cvt_cunction",end - start)
