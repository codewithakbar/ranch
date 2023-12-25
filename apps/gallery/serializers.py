from rest_framework import serializers
from .models import GalCategory, GalleryImages, VideoGallery


class GalleryImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = GalleryImages
        fields = '__all__'
        depth = 1


class CatGalleryImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = GalleryImages
        fields = ['category']
        depth = 1


class AllCatGalleryImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = GalCategory
        fields = '__all__'
        depth = 1



class VideoGallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoGallery
        fields = '__all__'
        depth = 1





