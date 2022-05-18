from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User


class User_profile_his(models.Model):
    log_id = models.AutoField(
        verbose_name=_('Log_id'),
        editable=False,
        primary_key=True,
        null=False,
    )

    log_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата создания'),
    )

    user_id = models.UUIDField(
        null=False,
        verbose_name=_('ID пользователя'),
        blank=True,
    )

    old_password = models.CharField(
        verbose_name=_('Старый пароль'),
        max_length=128,

    )
    new_password = models.CharField(
        verbose_name=_('Новый пароль'),
        max_length=128,

    )

    first_name = models.CharField(
        max_length=128,
        verbose_name=_("Имя"),
        blank=True,
        null=True,
    )
    second_name = models.CharField(
        max_length=128,
        verbose_name=_("Фамилия"),
        blank=True,
        null=True,
    )

    old_email = models.EmailField(
        verbose_name=_('Старый email address'),
        blank=True,
        null=True
    )
    new_email = models.EmailField(
        verbose_name=_('Новый email address'),
        blank=True,
        null=True
    )

    username = models.CharField(
        max_length=128,
        verbose_name=_("Никнейм"),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('User profile history')
        verbose_name_plural = _('Users profile histories')
