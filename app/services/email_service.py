from fastapi_mail import FastMail, MessageSchema
from app.utils.email_config import conf

async def send_email(email: str, code: str, name: str):
    message = MessageSchema(
        subject=f" Dear {name}, Your Vendor Code",
        recipients=[email],
        body=f"Hello {name},\n\nYour Vendor Code is: {code}",
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(message)