from django.contrib import admin
from .models import (
    Bannercha, HomeSlider,
    Category, Kunduz, KursNarxlari, Magistr, MalImages, Malumotlar, Content, 
                     Fakultetlar, Images, OchiqMalumot, OqishniKochirish, Rektorat, Sirtqi, ContentTable, Talabalar1, ZayavkaModel)

from modeltranslation.admin import TranslationAdmin

from mptt.admin import DraggableMPTTAdmin


# @admin.register(Banner)
# class BannerAdmin(admin.ModelAdmin):
#     pass


class ContentImagesInline(admin.StackedInline):
    model = Images


class ZayavkaModelInline(admin.StackedInline):
    model = ZayavkaModel


class ContentTableInline(admin.StackedInline):
    model = ContentTable
    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class MalumotlarImagesInline(admin.StackedInline):
    model = MalImages


class MalumotlarAdmin(TranslationAdmin):
    inlines = [MalumotlarImagesInline]
    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class ContentAdmin(TranslationAdmin):
    inlines = [ContentTableInline, ContentImagesInline, ZayavkaModelInline]
    group_fieldsets = True
    fields = ('title', 'desc', 'category', ('nomi', 'summa'), ("rektorimage", "lavozim", "desc_rek"), 'image')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class OchiqMalumotAdmin(TranslationAdmin):
    group_fieldsets = True
    fields = ('title', 'desc',  'image')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



class CategoryAdmin(DraggableMPTTAdmin, TranslationAdmin):
    group_fieldsets = True

    prepopulated_fields = {'slug': ('name',)}
    # list_display = ("name", )

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

    
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    fields = ('name', 'slug', 'parent')
    # inlines = [CategoryLangInline]
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Content,
                'category',
                'products_cumulative_count',
                cumulative=True)


        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Content,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs


    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'


    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'



class BannerAdmin(DraggableMPTTAdmin):
    fields = ('title', 'image', 'parent')
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title')


class ContentTableAdmin(TranslationAdmin):

    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

        

class KursNarxlariAdmin(TranslationAdmin):

    group_fieldsets = True
    fields = ('title_uz', 'title_ru', 'title_en', 'yonalish_uz', 'yonalish_ru', 'yonalish_en', 'kod', 'price', 'category')
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(ZayavkaModel)
class ZayavkaModelAdmin(admin.ModelAdmin):
    list_display = ('familiya', 'ismi', 'sharifi', 'telefon', 'email', 'pasport_seriya', 'pasport_raqami', 'tugilgan_yil', 'jinsi')
    search_fields = ('familiya', 'ismi', 'sharifi', 'telefon', 'email', 'pasport_seriya', 'pasport_raqami')
    


admin.site.register(Bannercha, BannerAdmin)
admin.site.register(Malumotlar, MalumotlarAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(ContentTable, ContentTableAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(HomeSlider)
admin.site.register(Talabalar1)
admin.site.register(OchiqMalumot, OchiqMalumotAdmin)
admin.site.register(Rektorat)
admin.site.register(KursNarxlari, KursNarxlariAdmin)
# admin.site.register(Kunduz)
# admin.site.register(Sirtqi)
# admin.site.register(OqishniKochirish)
# admin.site.register(Magistr)
# admin.site.register(Book)
