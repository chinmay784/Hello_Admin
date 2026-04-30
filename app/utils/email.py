import smtplib
from email.mime.text import MIMEText

EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"  # use app password (not real password)

def send_reset_email(to_email, token):
    reset_link = f"http://localhost:8000/reset-password?token={token}"

    msg = MIMEText(f"Click to reset password: {reset_link}")
    msg["Subject"] = "Password Reset"
    msg["From"] = EMAIL
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)