

from django.db import models
from django.conf import settings


class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owned_documents",
        null=True,
        blank=True,
    )

    shared_with = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="shared_documents",
        blank=True,
    )

    def __str__(self):
        return self.title

