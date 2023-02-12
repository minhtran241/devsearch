from typing import List
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from users.models import Profile


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=f"{user.first_name} {user.last_name}",
        )
        subject: str = "Welcome to DevSearch community!"
        message: str = f"""
        Dear {profile.name},Thank you for joining DevSearch community and welcome. DevSearch is the place you can connect with excellent developers around the world and have a chance to know about their outstanding projects. This platform aims the create a strong community where you can show your work with the world and have chances to have jobs.

        If you are an employer, DevSearch will recommends to you the most outstanding developers in the field you need. This tool provides the most handful features which makes your searching become easier!

        Thank you for your time,

        DevSearch Team.
        """
        email: EmailMessage = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[profile.email],
        )
        email.send(fail_silently=True)


@receiver(signal=post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        name_splitted: List[str] = profile.name.split(" ")
        user.first_name = name_splitted[0].strip().capitalize()
        if len(name_splitted) > 1:
            user.last_name = name_splitted[1].strip().capitalize()
        user.username = profile.username.strip().lower()
        user.email = profile.email
        user.save()


@receiver(signal=post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    try:
        instance.user.delete()
    except:
        pass


# post_save.connect(receiver=create_profile, sender=Profile)
# post_delete.connect(receiver=delete_user, sender=User)
