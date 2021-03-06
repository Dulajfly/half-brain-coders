from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _

from django.core.validators import MaxValueValidator, MinValueValidator

# class User(AbstractBaseUser):
#     pass

class ExitPoint(models.Model):
    DIFFICULT_CHOICES = [
        ('BE', _('BEGINNER')),
        ('IM', _('INTERMEDIATE')),
        ('AD', _('ADVANCED')),
        ('EX', _('EXPERT')),
        ('NR', _('NOT RECOMMENDED'))
    ]
    name = models.CharField(verbose_name=_('Name of exitpoint'),max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # country = CountryField(blank=Tru
    tracking_difficulty_level = models.CharField(verbose_name=_('Tracking skill level'), max_length=200, choices= DIFFICULT_CHOICES, blank=True, null=True)
    wingsuit_difficulty_level = models.CharField(verbose_name=_('Wingsuit skill level'), max_length=200, choices= DIFFICULT_CHOICES, blank=True, null=True)
    rock_drop_second = models.PositiveSmallIntegerField(verbose_name=_('Rock drop second'), validators=[MaxValueValidator(120), MinValueValidator(1)], null=True, blank=True)
    rock_drop_altitude = models.PositiveSmallIntegerField(verbose_name=_('Rock drop altitude'), validators=[MaxValueValidator(8849), MinValueValidator(10)], null=True, blank=True)
    landing_altitude = models.PositiveSmallIntegerField(verbose_name=_('Landing altitude'), validators=[MaxValueValidator(8000), MinValueValidator(1)], null=True, blank=True)
    lon = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)

    # def __str__(self):
    #     return self.name