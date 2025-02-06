# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Programs(models.Model):

    #__Programs_FIELDS__
    file name = models.TextField(max_length=255, null=True, blank=True)
    job number = models.IntegerField(null=True, blank=True)
    plan/part number = models.TextField(max_length=255, null=True, blank=True)
    part name = models.TextField(max_length=255, null=True, blank=True)
    comment = models.TextField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    customer = models.TextField(max_length=255, null=True, blank=True)

    #__Programs_FIELDS__END

    class Meta:
        verbose_name        = _("Programs")
        verbose_name_plural = _("Programs")



#__MODELS__END
