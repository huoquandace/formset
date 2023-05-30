from django.db import models
from django.utils.translation import gettext_lazy as _


class Parent(models.Model):
    name = models.CharField(_('name'), max_length=255)

class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(_('name'), max_length=255)