from django.db import models
from django.template.defaultfilters import slugify
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
    user = models.ForeignKey(User)
    date_time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __unicode__(self):
        return self.comment