from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsApi import AllYangilikViewSet, BannerchaViewSet, CategoryViewSet, ContentViewSet, HomeSliderViewSet, KursNarxlariViewSet, OchiqMalumotViewSet, RektoratViewSet, TalabalarViewSet, YangilikViewSet, ZayavkaPostView

from apps.gallery.views import AllGalleryCategoriesViewSet, GalleryImagesCategoriesViewSet, GalleryImagesViewSet, VideoGalleryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'talabalar', TalabalarViewSet, basename='talanalar')
router.register(r'bannerlar', BannerchaViewSet, basename='banner')
router.register(r'hamkorlar', HomeSliderViewSet, basename='hamkorlar-slides')
router.register(r'yangiliklar', AllYangilikViewSet, basename='yangiliklar')
router.register(r'rektorat', RektoratViewSet, basename='rektorat')
router.register(r'ochiq/malumot', OchiqMalumotViewSet, basename='ochiq')
# router.register(r'content', ContentViewSet, basename='content')
router.register(r'content/(?P<category_id>\d+)', ContentViewSet, basename='content')
router.register(r'yangilik/(?P<category_id>\d+)', YangilikViewSet, basename='yagnin')
router.register(r'narxla/(?P<category_id>\d+)', KursNarxlariViewSet, basename='narxla')
# router.register(r'zayavka', ZayavkaPostView, basename='zayavka')

router.register(r'gal/(?P<category_id>\d+)', GalleryImagesViewSet, basename='galirerya')
router.register(r'gal/cat/(?P<category_id>\d+)', GalleryImagesCategoriesViewSet, basename='galireryaCat')
router.register(r'all/cat/gal', AllGalleryCategoriesViewSet, basename='galireryaCA')



app_name = 'home'

urlpatterns = [

    path('', include(router.urls)),
    path('zayavka/', ZayavkaPostView.as_view(), name='zayavka-post'),


    
]



