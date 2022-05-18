from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.forms import ModelForm
from users.models.managers import UserManager
from utils.models import AbstractUUID, AbstractTimeTrackable
from django import forms


class User(PermissionsMixin, AbstractUUID, AbstractBaseUser, AbstractTimeTrackable):
    first_name = models.CharField(max_length=128, verbose_name=_("Имя"))
    second_name = models.CharField( max_length=128, verbose_name=_("Фамилия"), blank=True, null=True,)
    email = models.EmailField(verbose_name=_('email address'), unique=True)
    username = models.CharField(max_length=128, unique=True, verbose_name=_("Username"))
    password = models.CharField(max_length=100)
    follows = models.ManyToManyField("users.User", related_name="my_subscribers",verbose_name=_('Подписки'), blank=True)
    subscribers = models.ManyToManyField("users.User", related_name="my_followers", verbose_name=_('Подписчики'), blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log into this admin site.'), )
    is_active = models.BooleanField(_('active'), default=True ,help_text=('Designates whether this user should be treated as active. ' 'Unselect this instead of deleting accounts.'))

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return self.username


    def __str__(self):
        return self.username


class NewUserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'second_name', 'email', 'password')
