from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from users.models import User
from utils.models.abstract import AbstractTimeTrackable, AbstractUUID, AbstractCreatedByTrackable

STATUS_CHOICES = [
    ('ON', 'Opened'),
    ('INP', 'In progress'),
    ('DEL', 'Delayed'),
    ('OFF', 'Closed'),
    ('CND', 'Canceled'),
]


class Order(
    AbstractTimeTrackable, AbstractUUID, AbstractCreatedByTrackable, models.Model):
    title = models.CharField(
        verbose_name=_('Название'),
        max_length=128,
        blank=True,
        null=True,
    )
    deadline = models.DateTimeField(
        verbose_name=_('Дедлайн'),
    )

    max_cost = models.IntegerField(
        verbose_name=_('Лимит'),
        blank=True,
        null=True,
    )

    status = models.CharField(
        verbose_name=_('Статус'),
        max_length=3,
        choices=STATUS_CHOICES,
        default='ON'
    )
    details = models.TextField(
        verbose_name=_('Детали'),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')

    def __str__(self):
        return self.title


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['title', 'details', 'deadline', 'created_by', 'max_cost', ]
