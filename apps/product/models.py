from io import BytesIO
from PIL import Image

from django.core.files import File
from django.utils.text import slugify
from django.db import models

from django.contrib.auth.models import User

from apps.vendor.models import Vendor

GENDER_CHOICES = (
    ('men', 'men'),
    ('women', 'women'),
    ('kids', 'kids'),   # yeah that's not a gender but you could want to have this
)

class Attribute(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)
    attribute = models.ForeignKey(Attribute, related_name='category', on_delete=models.CASCADE, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['ordering']
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.title
        '''
        full_path = [self.title]            
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent

        return ' -> '.join(full_path[::-1])'''

    def get_absolute_url(self):
        return '/%s/' % (self.slug)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, related_name='products', on_delete=models.CASCADE)
    #gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_featured = models.BooleanField(default=False)
    num_available = models.IntegerField(default=1)
    num_visits = models.IntegerField(default=0)
    last_visit = models.DateTimeField(blank=True, null=True)
    
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product,self).save(*args, **kwargs)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)

    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)