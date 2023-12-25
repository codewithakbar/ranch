from django.db import models

from apps.home.models import Category
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel



class GalCategory(MPTTModel):
    
    name = models.CharField(max_length=211, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    slug = models.SlugField(null=False, unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "Galirerya Kategoriyasi"
        verbose_name_plural = "Galirerya Kategoriyalari"

    def __str__(self) -> str:
        return self.name


class TopBanner(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="gallery/%Y/%m%d")

    def __str__(self) -> str:
        return self.name



class GalleryImages(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="gallery/%Y/%m%d", blank=True, null=True)
    video = models.FileField(upload_to="gallery/video/%Y/%m/%d", blank=True, null=True)

    category = TreeForeignKey(to=GalCategory, on_delete=models.CASCADE, related_name="galCat", default=1)

    def __str__(self) -> str:
        return self.name



class VideoGallery(models.Model):
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to="gallery/video/%Y/%m/%d")
    thumbnail = models.ImageField(upload_to="thumbnail/")

    def __str__(self) -> str:
        return self.name

