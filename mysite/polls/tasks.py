from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task(bind=True)
def go_to_sleep(self, duration):
    sleep(duration)
    return "Done!"


@shared_task(bind=True)
def send_email_with_celery(self, subject, message, from_email, recipient_list):
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list
    )
    return "send_success"
