from django.utils.text import Truncator
from rest_framework import serializers

from apps.news.models import Yangiliklar
from .models import Category, Content, KursNarxlari, Malumotlar, Bannercha, Fakultetlar, Kunduz, OchiqMalumot, Sirtqi, OqishniKochirish, Magistr, Talabalar1, Rektorat, Book, Images, MalImages, HomeSlider, ContentTable, ZayavkaModel


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_children(self, obj):
        child_categories = obj.children.all()
        child_serializer = CategorySerializer(child_categories, many=True)
        return child_serializer.data


class ContentTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentTable
        fields = [
            'content',
            'kod',
            'yonalish',
            'price',
        ]

        
class KursNarxlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = KursNarxlari
        fields = [
            'title_uz',
            'title_ru',
            'title_en',
            'kod',
            'yonalish_uz',
            'yonalish_ru',
            'yonalish_en',
            'price',
        ]
        depth = 1


class ContentSerializer(serializers.ModelSerializer):
    contenttable = ContentTableSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = [
            'id',
            'title',
            'desc',
            'category',
            'image',
            'pdf',
            'nomi',
            'summa',
            'rektorimage',
            'lavozim',
            'desc_rek',
            'contenttable',
        ]
        depth = 1




class YangiliklarSerializer(serializers.ModelSerializer):
    mini_desc = serializers.SerializerMethodField()
    mini_title = serializers.SerializerMethodField()

    class Meta:
        model = Yangiliklar
        fields = ['id', 'title', 'desc', 'mini_title', 'mini_desc', 'image', 'post_url', 'category', 'base_category', 'created_at']
        depth = 1

    def get_mini_title(self, obj):
        return obj.title[:22]

    def get_mini_desc(self, obj):
        return obj.desc[:53]



class OchiqMalumotSerializer(serializers.ModelSerializer):
    mini_desc = serializers.SerializerMethodField()

    class Meta:
        model = OchiqMalumot
        fields = ['id', 'title', 'desc', 'mini_desc']

    def get_mini_desc(self, obj):
        return obj.desc[:53]



class MalumotlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Malumotlar
        fields = '__all__'



class BannerchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bannercha
        fields = '__all__'



class FakultetlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakultetlar
        fields = '__all__'



class KunduzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kunduz
        fields = '__all__'



class SirtqiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sirtqi
        fields = '__all__'



class OqishniKochirishSerializer(serializers.ModelSerializer):
    class Meta:
        model = OqishniKochirish
        fields = '__all__'



class MagistrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magistr
        fields = '__all__'



class TalabalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talabalar1
        fields = '__all__'



class RektoratSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rektorat
        fields = '__all__'



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'



class MalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MalImages
        fields = '__all__'



class HomeSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSlider
        fields = '__all__'








class ZayavkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZayavkaModel
        fields = ['familiya', 'ismi', 'sharifi', 'telefon', 'email', 'pasport_seriya', 'pasport_raqami', 'tugilgan_yil', 'jinsi']


        