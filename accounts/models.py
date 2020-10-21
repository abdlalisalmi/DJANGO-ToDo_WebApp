from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='users/avatars', null=True, blank=True)
    boi = models.CharField(max_length=500, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    # Social media websites
    github = models.URLField(max_length=255, null=True, blank=True)
    facebook = models.URLField(max_length=255, null=True, blank=True)
    twitter = models.URLField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return '/{}/'.format(self.user.username)


@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)