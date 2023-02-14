from typing import List
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.template.loader import get_template

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
        html_template = get_template(template_name="welcome_email.html")
        html_content = html_template.render({"profile": profile})
        email: EmailMessage = EmailMessage(
            subject=subject,
            body=html_content,
            from_email=settings.EMAIL_HOST_USER,
            to=[profile.email],
        )
        email.content_subtype = "html"
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
