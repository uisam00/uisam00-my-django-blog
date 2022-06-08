from django.db import models


# Create your models here.
class Link(models.Model):
    objects = None
    key = models.SlugField(verbose_name="Identificação Rede", max_length=100, unique=True)
    description = models.CharField(verbose_name="Descrição", max_length=250, null=True, blank=True)
    class_icon = models.CharField(verbose_name="Classe CSS do ícone", max_length=50, null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
        ordering = ['key']

    def __str__(selfs):
        return selfs.key
