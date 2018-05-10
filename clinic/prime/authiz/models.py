from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser

from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)

import uuid

# Create your models here.

# class UserManager(BaseUserManager):
#     def create_user(self, phone, password, **kwargs):
#         """
#         Creates and saves a Account with the given email or phone and password.
#         """

#         now = timezone.now()
#         if not email:
#             if not phone:
#                 raise ValueError('Users must have a valid email address or phone number.')
#         if not phone:
#             if not email:
#                 raise ValueError('Users must have a valid email address or phone number.')

#         user = self.model(phone=phone,
#             joined=now,
#             **kwargs
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

class Client(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(null=True, blank=True, unique=True)
    phone = models.CharField(max_length=18,unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=False, auto_now=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    password = models.CharField(default='', null=False, max_length=255)

    # USERNAME_FIELD = 'phone'

    # objects = UserManager()

    def get_username(self):
        return self.first_name

    def get_short_name(self):
        return self.last_name

    def __str__(self):
        return self.phone

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    def set_unusable_password(self):
        self.password = make_password(None)

    def has_usable_password(self):
        return is_password_usable(self.password)