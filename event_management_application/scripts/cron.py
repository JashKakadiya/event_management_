import mysql.connector
import smtplib
from email.mime.text import MIMEText

# Define the database connection parameters


# Define the email settings
smtp_host = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'student.gec416@gmail.com'
smtp_password = 'ceabwnkbmslawcib'

# Connect to the database
try:
    cnx = mysql.connector.connect(user='root', password='JASH@jash12',
                              host='localhost', database='new_event_management',
                              use_pure=True,auth_plugin='mysql_native_password')
    cursor = cnx.cursor()

    # Retrieve the rows with the specified criteria
    query = ("SELECT * FROM event_management_application_order "
             "WHERE status = 'success' AND email_sent = 0")
    cursor.execute(query)
    rows = cursor.fetchall()

    # Iterate over the rows and send an email for each row
    for row in rows:
        # Construct the email message
        message = MIMEText(f'''Hi, this is your order confirmation for order number {row[0]} , {row[1]} ,{row[2]} ,{row[3]} ,{row[4]} ,{row[5]} ,{row[6]} ,{row[6]} ,{row[7]} ,{row[8]},.''')
        message['Subject'] = 'Order Confirmation'
        message['From'] = smtp_username
        message['To'] = 'jashkk5@gmail.com'

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_host, smtp_port) as smtp_server:
            smtp_server.starttls()
            smtp_server.login(smtp_username, smtp_password)
            smtp_server.sendmail(smtp_username, ['jashkk5@gmail.com'], message.as_string())

        # Update the flag to indicate that the email has been sent
        update_query = ("UPDATE event_management_application_order "
                        f"SET email_sent = 1 WHERE id = {row[0]}")
        cursor.execute(update_query)
        cnx.commit()

    cursor.close()
    cnx.close()
    with open('/Users/jashkakadiya/Desktop/Python_training/event_management_/test.txt', 'w') as f:
        f.write('Success!')
        f.close()

    # with open('/Users/jashkakadiya/Desktop/Python_training/event_management_/test.txt', 'w') as f:
    #     f.write('\nHello World!')
    #     f.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
    with open('/Users/jashkakadiya/Desktop/Python_training/event_management_/test.txt', 'w') as f:
        f.write(f"Error: {err}")
        f.close()
