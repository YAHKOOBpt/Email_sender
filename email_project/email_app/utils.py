from django.core.mail import send_mail ,EmailMessage
from django.conf import settings

def send_email_to_user(email,subject, message):
    try:
        email_from = settings.EMAIL_HOST
        email_message = EmailMessage(subject, message, email_from, [email])
        email_message.attach_file("ANSWER.pdf")
        email_message.send()


    except Exception as e:
        print(e)