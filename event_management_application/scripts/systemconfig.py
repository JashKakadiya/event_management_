from ..models import SystemConfigs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import time 

def get_config():
    try:
        return SystemConfigs.objects.first()
    except Exception as e:
        print(f"Error retrieving system configuration: {e}")
        return None


def get_host_email():
    systemconfig_obj = get_config()
    

    return systemconfig_obj.system_config_EMAIL_HOST_USER if systemconfig_obj else ""
    

def get_host_password():
    systemconfig_obj = get_config()
    return systemconfig_obj.system_config_EMAIL_HOST_PASSWORD if systemconfig_obj else ""


def get_razor_key_id():
    systemconfig_obj = get_config()
    return systemconfig_obj.system_config_RAZOR_KEY_ID if systemconfig_obj else ""
        
    
def get_razor_key_secret():
    systemconfig_obj = get_config()
    return systemconfig_obj.system_config_RAZOR_KEY_SECRET if systemconfig_obj else ""

def get_host_companyName(request):
    systemconfig_obj = get_config()
    return {'company_name': systemconfig_obj.system_config_COMPANY_TITLE} if systemconfig_obj else ""

def get_host_companyAddress():
    systemconfig_obj = get_config()
    return systemconfig_obj.system_config_COMPANY_ADDRESS if systemconfig_obj else ""

def get_host_companyPhone(request):
    systemconfig_obj = get_config()
    return {'company_Phone': systemconfig_obj.system_config_COMPANY_PHONE} if systemconfig_obj else ""

def get_host_companyEmail():
    systemconfig_obj = get_config()
    return {'company_email': systemconfig_obj.system_config_COMPANY_EMAIL} if systemconfig_obj else ""

def get_host_paymentMethod():
    systemconfig_obj = get_config()
    return systemconfig_obj.system_config_PAYMENT_METHOD if systemconfig_obj else ""

def get_host_databaseUserName():
    systemconfig_obj = get_config()
    return systemconfig_obj.system_config_DATABASE_USER if systemconfig_obj else ""
    
def get_host_CompanyLogo(request):
    systemconfig_obj = get_config()
    return {'company_logo': systemconfig_obj.system_config_COMPANY_LOGO} if systemconfig_obj else ""
    
def get_host_Currency(request):
    systemconfig_obj = get_config()
    return {'payment_curruncy':systemconfig_obj.system_config_Currency} if systemconfig_obj else ""


def get_host_companyAddress_html(request):
    systemconfig_obj = get_config()
    return {'company_address':systemconfig_obj.system_config_COMPANY_ADDRESS} if systemconfig_obj else ""

def get_host_companyEmail_html(request):
    systemconfig_obj = get_config()
    return {'company_email':systemconfig_obj.system_config_COMPANY_EMAIL} if systemconfig_obj else ""


def get_host_companyLandline_html(request):
    systemconfig_obj = get_config()
    return {'company_landline':systemconfig_obj.system_config_COMPANY_LANDLINE} if systemconfig_obj else ""

def get_host_website():
    systemconfig_obj = get_config()
    return systemconfig_obj.system_config_HOST_WEBSITE if systemconfig_obj else "http://127.0.0.1:8000/"
         
    
def get_host_website_html(request):
    systemconfig_obj = get_config()
    return {'host_website':systemconfig_obj.system_config_HOST_WEBSITE} if systemconfig_obj else ""

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
