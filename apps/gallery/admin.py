from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import TopBanner, GalleryImages, VideoGallery, GalCategory

class GalleryImagesAdmin(DraggableMPTTAdmin):
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
        qs = GalCategory.objects.add_related_count(
                qs,
                GalleryImages,
                'category',
                'products_cumulative_count',
                cumulative=True)


        # Add non cumulative product count
        qs = GalCategory.objects.add_related_count(qs,
                 GalleryImages,
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



admin.site.register(TopBanner)
admin.site.register(GalleryImages)
admin.site.register(VideoGallery)
admin.site.register(GalCategory, GalleryImagesAdmin)
