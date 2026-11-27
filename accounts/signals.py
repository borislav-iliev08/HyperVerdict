from django.apps import apps
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Profile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_from_registration(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        if instance.role =='Customer':
            Group = apps.get_model("auth", "Group")
            cl_gr = Group.objects.get(name='Clients')
            instance.groups.add(cl_gr)
        else:
            Group = apps.get_model("auth", "Group")
            ex_gr = Group.objects.get(name='Experts')
            instance.groups.add(ex_gr)

