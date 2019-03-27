from django.db import models


class Cookie(models.Model):
    name = models.CharField("Nome", max_length=100, blank=True, null=True)
    archive = models.CharField("Arquivo", max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cookie"
        verbose_name_plural = "Cookies"
