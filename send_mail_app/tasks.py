from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    for user in users:
        subject = 'Hello Users'
        message = f'Hello {user.username}, thank you for being awesome!'
        to_email = user.email
        from_email = settings.EMAIL_HOST_USER  
        recipient_list = [to_email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

    return "Done"


