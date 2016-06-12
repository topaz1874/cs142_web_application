from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
import datetime
# Create your models here.
class User(models.Model):
    # id = models.IntegerField()
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=128)
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.__unicode__())
        super(User,self).save(*args, **kwargs)

class Photo(models.Model):
    # id = models.IntegerField()
    user = models.ForeignKey(User)
    date_time = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=256, unique=True)
    image = models.ImageField(null=True, blank=True)
    def __unicode__(self):
        return self.file_name

    def save(self, *args, **kwargs):
        date = datetime.datetime.now()
        self.file_name = '%s_%i' %  (self.file_name, date.microsecond)
        super(Photo,self).save(*args, **kwargs)

class Comments(models.Model):
    photo = models.ForeignKey(Photo)
    parent = models.ForeignKey("self", null=True, blank=True)
    user = models.ForeignKey(User)
    date_time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __unicode__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('userdetail', kwargs={'user_slug':self.photo.user.slug,})
    @property
    def is_child(self):
        if self.parent is not None:return True
        else: return False

    def get_children(self):
        if not self.is_child:
            return Comments.objects.filter(parent=self)
        return None


