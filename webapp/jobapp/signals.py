from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PostJob


@receiver(post_save, sender=PostJob)
def update_postjob_status(sender, instance, **kwargs):
    if instance.archived:
        instance.status = 'archived'
    else:
        instance.status = 'active'
    instance.save()
