from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.news.models import Yangiliklar
from .models import Category, Content, KursNarxlari, Malumotlar, Bannercha, Fakultetlar, Kunduz, OchiqMalumot, Sirtqi, OqishniKochirish, Magistr, Talabalar1, Rektorat, Book, Images, MalImages, HomeSlider, ContentTable, ZayavkaModel
from .serializers import (
    CategorySerializer,
    ContentSerializer,
    KursNarxlariSerializer,
    MalumotlarSerializer,
    BannerchaSerializer,
    FakultetlarSerializer,
    KunduzSerializer,
    OchiqMalumotSerializer,
    SirtqiSerializer,
    OqishniKochirishSerializer,
    MagistrSerializer,
    TalabalarSerializer,
    RektoratSerializer,
    BookSerializer,
    ImagesSerializer,
    MalImagesSerializer,
    HomeSliderSerializer,
    ContentTableSerializer,
    YangiliklarSerializer,
    ZayavkaSerializer,
)



class CategoryViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def list(self, request):
        cat_id = request.GET.get("cat")
        queryset = Category.objects.filter(parent=None)
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        cat_id = request.GET.get("cat")
        queryset = Category.objects.filter(id=cat_id)
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)



class ContentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = Content.objects.filter(category__id=category_id)
        return queryset


class KursNarxlariViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = KursNarxlari.objects.all()
    serializer_class = KursNarxlariSerializer


    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = KursNarxlari.objects.filter(category__id=category_id)
        return queryset


class YangilikViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSerializer


    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = Yangiliklar.objects.filter(base_category__id=category_id).order_by("-id")
        return queryset


class AllYangilikViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSerializer

  

class OchiqMalumotViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = OchiqMalumot.objects.all()
    serializer_class = OchiqMalumotSerializer



class MalumotlarViewSet(viewsets.ModelViewSet):
    queryset = Malumotlar.objects.all()
    serializer_class = MalumotlarSerializer



class BannerchaViewSet(viewsets.ModelViewSet):
    queryset = Bannercha.objects.all()[:8]
    serializer_class = BannerchaSerializer



class FakultetlarViewSet(viewsets.ModelViewSet):
    queryset = Fakultetlar.objects.all()
    serializer_class = FakultetlarSerializer



class KunduzViewSet(viewsets.ModelViewSet):
    queryset = Kunduz.objects.all()
    serializer_class = KunduzSerializer



class SirtqiViewSet(viewsets.ModelViewSet):
    queryset = Sirtqi.objects.all()
    serializer_class = SirtqiSerializer



class OqishniKochirishViewSet(viewsets.ModelViewSet):
    queryset = OqishniKochirish.objects.all()
    serializer_class = OqishniKochirishSerializer



class MagistrViewSet(viewsets.ModelViewSet):
    queryset = Magistr.objects.all()
    serializer_class = MagistrSerializer



class TalabalarViewSet(viewsets.ModelViewSet):
    queryset = Talabalar1.objects.all()
    serializer_class = TalabalarSerializer





class RektoratViewSet(viewsets.ModelViewSet):
    queryset = Rektorat.objects.all()
    serializer_class = RektoratSerializer
    



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class MalImagesViewSet(viewsets.ModelViewSet):
    queryset = MalImages.objects.all()
    serializer_class = MalImagesSerializer

class HomeSliderViewSet(viewsets.ModelViewSet):
    queryset = HomeSlider.objects.all()
    serializer_class = HomeSliderSerializer

class ContentTableViewSet(viewsets.ModelViewSet):
    queryset = ContentTable.objects.all()
    serializer_class = ContentTableSerializer






class ZayavkaPostView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ZayavkaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






