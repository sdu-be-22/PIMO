from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User
from django.forms import ModelForm
from utils.models.abstract import AbstractTimeTrackable, AbstractUUID

STAT_CHOICES = [
    ('A', 'Accepted'),
    ('W', 'Waiting'),
    ('D', 'Declined'),
]


class Offer(AbstractUUID, AbstractTimeTrackable, models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="User",
        verbose_name=_('Пользователь'),
        blank=True,
    )
    order_id = models.ForeignKey(
        'pimo.Order',
        on_delete=models.CASCADE,
        related_name="ID_order",
        verbose_name=_('ID заказа'),
        blank=True,
    )
    cost = models.IntegerField(
        verbose_name=_('Стоимость'),
        blank=True,
        null=True,
    )

    status = models.CharField(
        verbose_name=_('Статус заказа'),
        max_length=10,
        choices=STAT_CHOICES,
        default='W'
    )

    class Meta:
        verbose_name = _('Предложение')
        verbose_name_plural = _('Предложения')
        

class OfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = ['user_id', 'order_id', 'cost', ]
