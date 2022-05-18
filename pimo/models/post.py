from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User

from utils.models.abstract import AbstractTimeTrackable, AbstractUUID, AbstractCreatedByTrackable


class Post(AbstractUUID, AbstractCreatedByTrackable, AbstractTimeTrackable, models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=50,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_('Дата публикации')
    )
    details = models.TextField(
        verbose_name=_('Детали')
    )
    likes = models.BooleanField(
        'Likes'
    )

    class Meta:
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')

    def __str__(self):
        return self.title
