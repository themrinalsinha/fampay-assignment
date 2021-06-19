from django.db                       import models
from django.contrib.postgres.indexes import HashIndex, BTreeIndex


class KeyStatus(models.TextChoices):
    ACTIVE          = 1, "Active"
    DEACTIVATED     = 2, "Deactivated"
    QUOTA_EXHAUSTED = 3, "Quota Exhausted"

class BaseModel(models.Model):
    created_on  = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class KeyManager(BaseModel):
    name       = models.CharField(max_length=64, blank=True, null=True)
    access_key = models.CharField(max_length=64)
    status     = models.CharField(max_length=1, choices=KeyStatus.choices,
                                  default=KeyStatus.ACTIVE)

    def __str__(self) -> str:
        return f"KeyManager({self.name} - {self.status})"

    class Meta:
        verbose_name        = "Key Manager"
        verbose_name_plural = "Key Manager"


class YoutubeFeed(BaseModel):
    video_id     = models.CharField(max_length=128, unique=True)
    title        = models.CharField(max_length=128)
    description  = models.TextField()
    thumbnails   = models.JSONField()
    published_at = models.DateTimeField()
    meta_info    = models.JSONField(blank=True, null=True)

    def __str__(self) -> str:
        return f"YoutubeFeed({self.title})"

    class Meta:
        indexes = (
            BTreeIndex(fields=('video_id',)),
            BTreeIndex(fields=('title',)),
            HashIndex(fields=('description',))
        )

        ordering            = ('-published_at',)
        verbose_name        = "YouTube Feed"
        verbose_name_plural = "YouTube Feed(s)"
