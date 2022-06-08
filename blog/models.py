from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset() \
            .filter(status='publicado')

class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )
    title = models.CharField(verbose_name="Título", max_length=100, unique=True)
    slug = models.SlugField(max_length=200,
                            unique=True)
    subtitle = models.CharField(max_length=250)

    author = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name="get_posts", verbose_name="Categoria")
    image = models.ImageField(verbose_name="Imagem", upload_to="blog", blank=True, null=True)
    article = RichTextField(verbose_name="Conteúdo")
    posted = models.DateTimeField(verbose_name="Data de publicação", default=timezone.now)
    created = models.DateTimeField(verbose_name="Data de criação", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Última atualização", auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='rascunho')
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-posted',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.slug])

    def get_absolute_url_update(self):
        return reverse("post_edit", args=[self.slug])

    def get_absolute_url_delete(self):
        return reverse("post_delete", args=[self.slug])

    @property
    def view_image(self):
        return mark_safe('<img src="%s" width="400px" />'%self.image.url)
        view_image.short_description = "Imagem Cadastrada"
        view_image.allow_tags = True

@receiver(post_save, sender=Post)
def insert_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        return instance.save()
