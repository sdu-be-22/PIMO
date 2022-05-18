from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User


class User_backup(models.Model):
    log_id = models.AutoField(
        verbose_name=_('Log_id'),
        editable=False,
        primary_key=True,
        null=False,
    )
    user_id = models.UUIDField(
        null=False,
        verbose_name=_('ID пользователя'),
        blank=True,
    )
    username = models.CharField(
        verbose_name=_('Никнейм'),
        max_length=50,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата создания'),
    )

    deleted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата удаления'),
    )

    class Meta:
        verbose_name = _('User backup')
        verbose_name_plural = _('User backups')
