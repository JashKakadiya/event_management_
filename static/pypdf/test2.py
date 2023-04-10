# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import pdfkit
def Mail_send(data,email_from,email_to,email_password):
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = email_from

    # storing the receivers email address
    msg['To'] = email_to

    # storing the subject
    msg['Subject'] =  'Event Management Payment'

    # string to store the body of the mail
    body = f'''Hi {data.user_name}, thank you for registering in Event.

your order is successfully placed.
            
order id: {data.provider_order_id}      
order amount: {int(data.amount)}/- rupees only
order status: {data.status}
Phone number: {data.user_phone}
                            
                            
                            
                            '''

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(os.path.abspath(os.path.dirname('invoice.pdf/')), "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % "invoice.pdf")
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email_from, email_password)
    text = msg.as_string()

    s.sendmail(email_from,email_to, text)

    # terminating the session
    s.quit()

pdfkit.from_string('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/event_management_/static/css/invoice/new_css.css">
        <style>
      @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300&family=Poppins:wght@200;300;400;500;600&display=swap');
*{
  font-family: 'Poppins', sans-serif;
}
body{
    border: 1px solid black;
  background-repeat: no-repeat;
  background-color: rgb(210, 207, 207);
}
td,th{
  /* border: 1px solid rgb(236, 27, 27); */
  padding-left: 30px;
}
    </style>
    </head>
<body>
    <div>
        <table >
            <tr>
                <th style="text-align: left; padding-left: 30px;"><h2>{company_logo['company_name']}</h2></th>
                <th style="text-align: left; padding-right: 30px;"><h3>Booking id: </h3></th>
            </tr>
            <tr>
                <td style="text-align: left; padding-left: 30px;" colspan="2"><strong>
                    <span><h2>Hey, Your booking is confirmed.</h2></span>
                </strong>
            <h3>
                    Collect your tickets at the venue.</td>
                </h3>
            </tr>
            <tr>
                <td  style="text-align: left; padding-left: 30px;"><h2></h2></td>
                <td style="font-size: larger;"><strong>Vanue :- </strong><a href="">Directions</a></td>
                
            </tr>
            <tr>
                <td rowspan="2" style="align-items: left; padding: 10px;"><img style="height: 350px; width: 330px; border-radius: 20px;" src="data:image/png;base64,{img_base64 alt=""></td>
                <td><h3><strong>Address :- </strong></h3><p></p></td>
                
            </tr>
            <tr>
                <td colspan="2"><h3><strong>Time :-  </strong> {data.eve</h3></td>
            </tr>
            <table style="width: 100%; margin-top: 30px;">
                <tr>
                    <th style="text-align: center;">Category</th>
                    <th>Quantity</th>
                    <th>Price</th>
                </tr>
                <tr>
                    <th style="text-align: center; background-color: gray; height: 50px; border-radius: 5px; width: 200px;">{data.ticket_type</th>
                    <th style="text-align: center; background-color: gray; height: 50px; border-radius: 5px;">{data.ticket_count</th>
                    <th style="text-align: center; background-color: gray; height: 50px; border-radius: 5px width: 200px;">Rs. {data.amount</th>
                </tr>
                <tr>
                    <td></td>
                    <td style="text-align: center;"><img style="width: 200px; height: 200px;" src="{os.path.abspath(os.path.dirname('event_management_application/media/'))}/{data.payment_id.png"  alt=""></td>
                    <td></td>
                </tr>
            </table>
            <table style="width: 100%; padding: 30px;">
                <tr>
                    <th style="text-align: left; border-top: 1px solid black; border-bottom: 1px solid black;background-color: gray;"><strong><h1>Total Amount Paid</h1></strong></th>
                    <th style="text-align: end; border-top: 1px solid black; border-bottom: 1px solid black;background-color: gray;"><strong><h1>Rs. {(data.amount)+((data.amount)*0.18)}</h1></strong></th>
                    
                </tr>
                <tr>
                    <td style="color: gray;"><span>Price</span></td>
                    <td style="text-align: end; color: gray;"><span>Rs. {(data.amount)}</span></td>
                </tr>
                <tr>
                    <td style="color: gray;"><span>Tax</span></td>
                    <td style="text-align: end; color: gray;"><span>Rs. {(data.amount)*0.18}</span></td>
                </tr>
            </table>
        </table>
    </div>
   
    
 
</body>
</html>
    
    
    ''', 'invoice32e.pdf' ,options={"enable-local-file-access": ""})




