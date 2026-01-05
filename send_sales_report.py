import smtplib
from email.message import EmailMessage
import ssl
import os

sender = input("Enter sender email address: ")
password = input("Enter App password: ")
receiver = input("Enter receiver email address: ")
subject = input("Enter Email subject: ")
body = input("Enter Email body: ")
file_loc = input("Enter folder path containing sales_summary.xlsx: ")

file_path = os.path.join(file_loc, "sales_summary.xlsx")

if not os.path.exists(file_path):
    print("Error: sales_summary.xlsx not found.")
    exit()

msg = EmailMessage()
msg.set_content(body)
msg["Subject"] = subject
msg["From"] = sender
msg["To"] = receiver

with open(file_path, "rb") as f:
    file_data = f.read()

msg.add_attachment(
    file_data,
    maintype="application",
    subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    filename="sales_summary.xlsx"
)

try:
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(context=context)
        server.login(sender, password)
        server.send_message(msg)

    print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email: {e}")
