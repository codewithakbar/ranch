from rest_framework import viewsets, permissions

from django.shortcuts import render

from apps.home.models import Bannercha, Category, HomeSlider, Malumotlar
from apps.news.models import Yangiliklar

from .models import GalCategory, TopBanner, GalleryImages, VideoGallery
from .serializers import AllCatGalleryImagesSerializer, GalleryImagesSerializer, VideoGallerySerializer, CatGalleryImagesSerializer



class GalleryImagesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # queryset = GalleryImages.objects.all()
    serializer_class = GalleryImagesSerializer


    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = GalleryImages.objects.filter(category__id=category_id)
        return queryset


class GalleryImagesCategoriesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # queryset = GalleryImages.objects.all()
    serializer_class = CatGalleryImagesSerializer


    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = GalCategory.objects.filter(id=category_id)
        return queryset



class AllGalleryCategoriesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = GalCategory.objects.all()
    serializer_class = AllCatGalleryImagesSerializer



class VideoGalleryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # queryset = GalleryImages.objects.all()
    serializer_class = VideoGallerySerializer


    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = VideoGallery.objects.filter(category__id=category_id)
        return queryset




def gallery(request):
    context = {
        'topbanner': TopBanner.objects.all().order_by('-id')[:10],
        'gal_image': GalleryImages.objects.all().order_by('-id'),
        'videos': VideoGallery.objects.all().order_by('-id'),


        'categories': Category.objects.filter(parent=None)[:5],
        "news": Yangiliklar.objects.all().order_by("?")[:3],
        "malumotlar": Malumotlar.objects.all().order_by("-id")[:3],
        "bannercha": Bannercha.objects.all()[:8],
        "sliders": HomeSlider.objects.all().order_by("-id")[:7]
    }

    return render(request, "gallery/glavnaya.html", context)


def foto(request):
    context = {
        'topbanner': TopBanner.objects.all().order_by('-id')[:10],
        'gal_image': GalleryImages.objects.all().order_by('-id'),
        'videos': VideoGallery.objects.all().order_by('-id'),


        'categories': Category.objects.filter(parent=None)[:5],
        "news": Yangiliklar.objects.all().order_by("?")[:3],
        "malumotlar": Malumotlar.objects.all().order_by("-id")[:3],
        "bannercha": Bannercha.objects.all()[:8],
        "sliders": HomeSlider.objects.all().order_by("-id")[:7]
    }

    return render(request, "gallery/foto.html", context)


def video(request):
    context = {
        'topbanner': TopBanner.objects.all().order_by('-id')[:10],
        'gal_image': GalleryImages.objects.all().order_by('-id'),
        'videos': VideoGallery.objects.all().order_by('-id'),


        'categories': Category.objects.filter(parent=None)[:5],
        "news": Yangiliklar.objects.all().order_by("?")[:3],
        "malumotlar": Malumotlar.objects.all().order_by("-id")[:3],
        "bannercha": Bannercha.objects.all()[:8],
        "sliders": HomeSlider.objects.all().order_by("-id")[:7]
    }

    return render(request, "gallery/video.html", context)