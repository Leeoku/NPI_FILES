from django.db import models


class DownloadURL(models.Model):
    file_name = models.CharField(max_length=100)
    created_by = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    url = models.URLField()
    downloaded = models.BooleanField(default=False)

    def __str__(self):
        return self.file_name
