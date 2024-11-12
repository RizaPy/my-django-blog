from django.core.mail import send_mail
from myBlog.celery import app


@app.task()
def send_email(subject, message, recipient_list):
    send_mail(
            subject,
            message,
            'rizamat4@gmail.com',
            recipient_list

    )
