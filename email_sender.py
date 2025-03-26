import smtplib
from email.message import EmailMessage

# Replace with your email credentials
EMAIL_ADDRESS = "youremail@gmail.com"
EMAIL_PASSWORD = "yourpassword"

msg = EmailMessage()
msg['Subject'] = 'Daily Report'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'receiver@example.com'
msg.set_content('Please find today\'s report attached.')

# Attach a file (change 'report.xlsx' to your file)
with open('report.xlsx', 'rb') as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

# Send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("Email sent!")
