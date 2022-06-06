from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset() \
            .filter(status='posted')


class Post(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('posted', 'Posted')
    )
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250,
                            unique=True)
    subtitle = models.CharField(max_length=250)

    author = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    article = models.TextField()
    posted = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='draft')
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

@receiver(post_save, sender=Post)
def insert_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        return instance.save()
