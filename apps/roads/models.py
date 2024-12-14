import os
import uuid

from django.db import models


class Roads(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to='static/img/')
    search_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Road"
        verbose_name_plural = "Roads"

    def save(self, *args, **kwargs):
        if self.image and not self.image.name.startswith("static/img/"):
            ext = os.path.splitext(self.image.name)[-1]
            self.image.name = f"{uuid.uuid4().hex}{ext}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
