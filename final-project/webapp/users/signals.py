from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User

from webapp.users.models import UserPerson, UserAgent


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_useragent:
            UserAgent.objects.create(user=instance)
        elif instance.is_userperson:
            UserPerson.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_useragent:
        instance.useragent.save()
    elif instance.is_userperson:
        instance.userperson.save()
