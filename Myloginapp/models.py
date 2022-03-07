from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
class CustomUser(AbstractBaseUser,PermissionsMixin):
    username =models.CharField(max_length=250)
    email = models.EmailField(_('email address'), unique=True)
    mobile =models.CharField(max_length=10)
    status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    object =CustomUserManager()

class ApplicationId(models.Model):
     Full_name = models.CharField(max_length=100),
     Facebook_APP_ID = models.CharField(max_length=200),
     LinkedIn_APP_ID = models.CharField(max_length=200),
     Twitter_APP_ID = models.CharField(max_length=200),
     Intagram_APP_ID = models.CharField(max_length=200),
