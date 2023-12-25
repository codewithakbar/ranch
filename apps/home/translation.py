from .models import Category, Content, KursNarxlari, Malumotlar, ContentTable, OchiqMalumot
from apps.news.models import NewsCartegory, Yangiliklar
from apps.gallery.models import TopBanner, GalleryImages, VideoGallery
from modeltranslation.translator import TranslationOptions,register


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')


@register(Content)
class ContentTranslationOptions(TranslationOptions):
    fields = ('title', 'desc', 'nomi', 'lavozim', 'desc_rek')


@register(OchiqMalumot)
class OchiqMalumotTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')


@register(ContentTable)
class ContentTableTranslationOptions(TranslationOptions):
    fields = ('yonalish',)


@register(KursNarxlari)
class KursNarxlariTranslationOptions(TranslationOptions):
    fields = ('yonalish', 'title')


@register(Malumotlar)
class MalumotlarTranslationOptions(TranslationOptions):
    fields = ('title', 'desc',)


@register(NewsCartegory)
class NewsCartegoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')


@register(Yangiliklar)
class YangiliklarTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')


# Gallery
@register(TopBanner)
class TopBannerTranslationOptions(TranslationOptions):
    fields = ('name',)
    

@register(GalleryImages)
class GalleryImagesTranslationOptions(TranslationOptions):
    fields = ('name',)
    
@register(VideoGallery)
class VideoGalleryTranslationOptions(TranslationOptions):
    fields = ('name',)
