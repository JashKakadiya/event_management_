from django.conf import settings
import os
import qrcode
import hashlib
from ..models import *
import base64
import random
from urllib.parse import urlencode

from requests import request
import requests
from ..models import *
# from django.conf import settings


from PIL import Image, ImageDraw
from django.core.files import File

import pdfkit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders
from datetime import datetime
import hashlib

import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from .systemconfig import *

def invoive_qrcode(data,order):
    img = qrcode.make(data)
    img_name = f"{order.payment_id}.png"
    img.save(os.path.abspath(os.path.dirname(__file__))+'/media'+'/'+ img_name)
    

def generate_hash(data):
    data = "{}".format(data).encode()
    return hashlib.sha256(data).hexdigest()


def generate_url(data):
    base_url = f"{get_host_website()}/customer/"
    params = {
        "data":data
    }
    response = base_url + "?" + urlencode(params)
    return response

# def generate_qrcode1(data,id):
#     ticket = Order.objects.get(event_id=int(id))
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=5,
#         border=4,
#     )
#     qr.add_data(str(data))
#     qr.make(fit=True)

#     img = qr.make_image(fill_color="black", back_color="white")

#     canvas=Image.new("RGB", (230,230),"white")
#     draw=ImageDraw.Draw(canvas)
#     canvas.paste(img)
#     buffer=BytesIO()
#     canvas.save(buffer,"PNG")
#     ticket.ticket_qrcode.save(f'image{id}.png',File(buffer),save=False)
#     canvas.close()
#     ticket.save()






