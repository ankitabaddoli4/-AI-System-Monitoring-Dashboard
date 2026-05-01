import smtplib
from email.mime.text import MIMEText

def send_email_alert(message):
    sender = "your_email@gmail.com"
    password = "your_app_password_here"  
    receiver = "receiver_email@gmail.com"

    msg = MIMEText(message)
    msg["Subject"] = "⚠️ CPU Alert"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        print("Connecting...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        print("Logging in...")
        server.login(sender, password)

        print("Sending...")
        server.sendmail(sender, receiver, msg.as_string())

        server.quit()

        print("✅ Email Sent")

    except Exception as e:
        print("❌ Error:", e)
