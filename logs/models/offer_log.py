from django.db import models
from django.utils.translation import gettext_lazy as _

from pimo.models import Offer



class Offer_log(models.Model):
    log_id = models.AutoField(
        verbose_name=_('Log_id'),
        editable=False,
        primary_key=True,
        null=False,
    )

    action = models.CharField(
        verbose_name=_('Действия'),
        max_length=300,
    )

    offer = models.UUIDField(
        null=False,
        verbose_name=_('ID предложения'),
        blank=True,
    )

    cost = models.IntegerField(
        verbose_name=_('Стоимость'),
        blank=True,
        null=True,
    )

    datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Последняя активность'),
    )
    last_status = models.CharField(
        verbose_name=_('Последний Статус'),
        max_length=32,
    )

    class Meta:
        verbose_name = _(' История предложения')
        verbose_name_plural = _('Истории предложений')