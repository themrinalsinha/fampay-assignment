from django.db import models


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
