from django.db import models
from django.utils.translation import gettext_lazy as _

from pimo.models import Order
from users.models import User


class Order_log(models.Model):
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

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата создания'),
    )

    deleted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата удаления'),
    )

    last_status = models.CharField(
        verbose_name=_('Последний Статус'),
        max_length=32,
    )

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=128,
        blank=True,
        null=True,
    )

    user_id = models.UUIDField(
        null=False,
        verbose_name=_('ID автора'),
        blank=True,
    )

    deadline = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name=_('Deadline'),
    )

    class Meta:
        verbose_name = _(' История заказа')
        verbose_name_plural = _('Истории Заказов')
