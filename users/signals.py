
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail

# Signal qabul qiluvchisi (receiver)
@receiver(post_save, sender=User)
def welcome_email(sender, instance, created, **kwargs):
    if created:
        # Yangi foydalanuvchi yaratildi, unga xush kelibsiz email jo'natamiz
        send_mail(
            'Welcome!',
            'Thanks for signing up to our website.',
            'rizamat4@gmail.com',
            [instance.email],
        )
