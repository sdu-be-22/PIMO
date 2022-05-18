from django.db import models
from django.utils.translation import gettext_lazy as _


class Offer_his(models.Model):
    log_id = models.AutoField(
        verbose_name=_('Log_id'),
        editable=False,
        primary_key=True,
        null=False,
    )
    offer = models.UUIDField(
        null=False,
        verbose_name=_('ID предложения'),
        blank=True,
    )
    old_status = models.CharField(
        verbose_name=_('Прежний Статус'),
        max_length=32,
    )
    new_status = models.CharField(
        verbose_name=_('Новый Статус'),
        max_length=32,
    )
    log_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Последняя активность'),
    )

    class Meta:
        verbose_name = _(' История изменения предложения')
        verbose_name_plural = _('Истории изменений предложений')
