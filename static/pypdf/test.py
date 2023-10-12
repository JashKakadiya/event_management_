import pdfkit
import os
import base64
from datetime import datetime
import time
def convert_to_pdf(data,company_logo,event,location):
    start = time.time()
    datetime_str = str(data.event_From)
    # datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

    # new_datetime_str = datetime_obj.strftime('%d %B %Y %I:%M %p')
    # new_datetime_str = new_datetime_str.replace(" 0", " ")

    # ordinal_indicator = 'th' if 11<=datetime_obj.day<=13 else {1:'st', 2:'nd', 3:'rd'}.get(datetime_obj.day % 10, 'th')
    # new_datetime_str = new_datetime_str[:2] + ordinal_indicator + new_datetime_str[2:]

    with open(f"{os.path.abspath(str(location.Image))}", 'rb') as f:
        img_data = f.read()
        img_base64 = base64.b64encode(img_data).decode('utf-8')
    end = time.time()
    print("pre", end - start)
    start = time.time()
    pdfkit.from_string(
    
f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
        <style>
      
*{{
  font-family: 'Poppins', sans-serif;
}}
body{{

  background-repeat: no-repeat;
  background-color: rgb(210, 207, 207);
}}
td,th{{
  /* border: 1px solid rgb(236, 27, 27); */
  padding-left: 30px;
}}
    </style>
    </head>
<body>
    <div>
        <table>
            <tr>
                <th style="text-align: left; padding-left: 30px;"><img style="height: 70px; width: 70px;" src="{(os.path.abspath(os.path.dirname('static/logo/logo.png/')))}" alt=""><h2>{company_logo['company_name']}</h2></th>
                <th style="text-align: left; padding-right: 30px;"><h3>Booking id: {data.payment_id}</h3></th>
            </tr>
            <tr>
                <td style="text-align: left; padding-left: 30px;" colspan="2"><strong>
                    <span><h2>Hey {data.user_name} , Your booking is confirmed.</h2></span>
                </strong>
            <h3>
                    Collect your tickets at the venue.</td>
                </h3>
            </tr>
            <tr>
                <td  style="text-align: left; padding-left: 30px;"><h2>{data.event_name}</h2></td>
                <td style="font-size: larger;"><strong>Vanue :- </strong><a href="{event.location_link}">Directions</a></td>
                
            </tr>
            <tr>
                <td rowspan="2" style="align-items: left; padding: 10px;"><img style="height: 350px; width: 330px; border-radius: 20px;" src="data:image/png;base64,{img_base64} alt=""></td>
                <td><p>{event.address}</p></td>
                
            </tr>
            <tr>
                <td colspan="2"><h3>{datetime_str}</h3></td>
            </tr>
            <table style="width: 100%; margin-top: 30px; padding: 30px;">
                <tr>
                    <th style="text-align: center;">Category</th>
                    <th>Quantity</th>
                    <th>Price</th>
                </tr>
                <tr>
                    <th style="text-align: center; background-color: gray; height: 50px; border-radius: 5px; width: 200px; font-size: 25px;">{data.ticket_type}</th>
                    <th style="text-align: center; background-color: gray; height: 50px; border-radius: 5px; font-size: 25px;">{data.ticket_count}</th>
                    <th style="text-align: center; background-color: gray; height: 50px; border-radius: 5px width: 200px; font-size: 25px;">Rs. {data.amount}</th>
                </tr>
                <tr>
                    <td></td>
                    <td style="text-align: center;"><img style="width: 200px; height: 200px;" src="{os.path.abspath(os.path.dirname('event_management_application/media/'))}/{data.payment_id}.png"  alt=""></td>
                    <td></td>
                </tr>
            </table>
            <table style="width: 100%; padding: 30px;">
                <tr>
                    <th style="text-align: left; border-top: 1px solid black; border-bottom: 1px solid black;"><strong><h3>Total Amount Paid</h3></strong></th>
                    <th style="text-align: end; border-top: 1px solid black; border-bottom: 1px solid black;"><strong><h3>Rs. {(data.amount)}</h3></strong></th>
                    
                </tr>
                <tr>
                    <td style="color: gray;"><span>Price</span></td>
                    <td style="text-align: end; color: gray;"><span>Rs. {int((data.amount/118)*100)}</span></td>
                </tr>
                <tr>
                    <td style="color: gray;"><span>Tax</span></td>
                    <td style="text-align: end; color: gray;"><span>Rs. {int(data.amount - ((data.amount/118)*100))}</span></td>
                </tr>
            </table>
        </table>
    </div>
</body>
</html>    
''', os.path.abspath(os.path.dirname('static/invoices/'))+f'/{data.payment_id}.pdf', options={"enable-local-file-access": ""})
    end = time.time()   
    print("post", end - start)


    

