import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class AbstractTimeTrackable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now_add=True),

    class Meta:
        abstract = True


class AbstractUUID(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name=_("Уникальное поле"),
    )

    class Meta:
        abstract = True


class AbstractCreatedByTrackable(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null = True)

    class Meta:
        abstract = True
