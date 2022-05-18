from django.db import models
from django.utils.translation import gettext_lazy as _

from pimo.models import Order



class Order_his(models.Model):
    log_id = models.AutoField(
        verbose_name=_('Log_id'),
        editable=False,
        primary_key=True,
        null=False,
    )
    order_id = models.UUIDField(
        null=False,
        verbose_name=_('ID заказа'),
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
        verbose_name = _('История изменения заказа')
        verbose_name_plural = _('Истории изменений заказов')
