from django.db import models
import os
from django.conf import settings
from .helper import resize
from django.core.files import File
from django.contrib.auth.models import User



Choice = (
(1, 'Kishi ucun'),
(2, 'Qadin ucun'),
(3, 'Ushaq ucun')
)

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    madein = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='image/',null=True, blank=True)

    def __str__(self):
        return self.title



class IntegerRangeField(models.IntegerField):

    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class UploadPicture(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    madein = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True)
    star = IntegerRangeField(min_value=1, max_value=5,  null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image/',null=True, blank=True)
    thumb_image = models.ImageField(upload_to='thumb_image/',null=True, blank=True, editable=False)
    slider_image = models.ImageField(upload_to='slider_image/',null=True, blank=True, editable=False)
    post_image = models.ImageField(upload_to='post_image/',null=True, blank=True, editable=False)
    status = models.BooleanField(default=False)
    choose = models.IntegerField(choices=Choice, default=1)
    #fileinstance , signal
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(UploadPicture, self).save( *args, **kwargs)
        image_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
        slide_path = 'slide_' + self.image.name[8:]
        slider_image_path = os.path.join(settings.MEDIA_ROOT, slide_path)
        resize(image_path,slider_image_path, 820, 450)
        self.slider_image = File(open(slider_image_path, 'rb'))
        self.slider_image.name  = self.slider_image.name[46:]

        thumb_path = 'thumb_' + self.image.name[8:]
        thumb_image_path = os.path.join(settings.MEDIA_ROOT, thumb_path)
        resize(image_path,thumb_image_path, 450, 300)
        self.thumb_image = File(open(thumb_image_path, 'rb'))
        self.thumb_image.name = self.thumb_image.name[46:]

        post_path = 'post_' +self.image.name[7:]
        post_image_path = os.path.join(settings.MEDIA_ROOT, post_path)
        resize(image_path, post_image_path, 750, 500)
        self.post_image = File(open(post_image_path, 'rb'))
        self.post_image.name = self.post_image.name[46:]
        try:
            os.remove(slider_image_path)
            os.remove(thumb_image_path)
            os.remove(post_image_path)
        except:
            pass
        super(UploadPicture, self).save( *args, **kwargs)

    #def save(self, *arg, **kwargs):
        #super(UploadPicture, self).save( *args, **kwargs)
        #image_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
        #thumb_path = 'thumb_' + self.image.name[8:]
        #thumb_image_path = os.path.join(settings.MEDIA_ROOT, thumb_path)
        #rsize(image_path,thumb_image_path, 600, 300)
        #self.thumb_image = File(open(thumb_image_path, 'rb')
        #self.thumb_image.name = self.thumb_image.name[46:]
        #super(UploadPicture, self).save( *args, **kwargs)
