from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'post/{filename}'.format(filename = filename)



User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"
        ordering=["name"]

    def __str__(self):
        return self.name


class Post(models.Model):
    #custom object manager
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")


    options=(
        ('draft','Draft'),
        ('published','Published'),
    )
    category = models.ForeignKey(Category , on_delete = models.PROTECT , default = 1 )
    title =  models.CharField(max_length=250)
    image = models.ImageField(_("Image"),upload_to=upload_to , default="post/default.jpg")
    excerpt =  models.TextField(null=True)
    content =  models.TextField(null=True)
    slug = models.SlugField(max_length=250 , unique_for_date = 'published')
    published = models.DateTimeField(default=timezone.now)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name = "blog_post")
    status = models.CharField(max_length=10 , choices=options , default = "published")
    objects = models.Manager() # default manager
    postobjects = PostObjects() # custom manager

    class Meta:
        ordering  = ('-published',)

    def __str__(self):
        return self.title


    
