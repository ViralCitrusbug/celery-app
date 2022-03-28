import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from time import sleep
from django.core.mail import send_mail
from celery import shared_task

@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format (total)

@shared_task
def sleepy(duration):
    sleep(duration)
    return f"function Completed"

@shared_task  
def send_email(subject,body,receiver):
    sender='sample31730273'
    send_mail(
        subject,body,sender,[receiver]
    )