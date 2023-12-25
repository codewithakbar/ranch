"""
URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import URLPattern, URLResolver, include, path, re_path
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

from ranch.application import DEBUG
from ranch.web import STATIC_ROOT, STATIC_URL
from apps.home import views as HomwViews
from apps.home import views
from apps.news import views as NewsView
from apps.gallery import views as GalleryView



urlpatterns: list[URLResolver | URLPattern] = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.web.urls")),

    path("malumotlar/", views.malumotlar, name="malumotlar"),
    path("malumotlar/<int:cat_id>/", views.malumotlar, name="malumot"),
    path("malumot/<int:cat_id>/", views.malumot_detail, name="malumot_detail"),

    path("category/<int:cat_id>/", views.category, name="category"),

    path("gal/", GalleryView.gallery, name="gal"),
    path("foto/", GalleryView.foto, name="foto"),
    path("video/", GalleryView.video, name="video"),

    path('ranch/web/ru/', views.get_url),
    path('ranch/web/uz/', views.get_url),
    path('ranch/web/site/aloqa/', views.get_url),
    path('moodle/?lang=ru/', views.get_url),
    path('ranch/web/site/abitur?id=6/', views.get_url),
    path('ranch/web/qabul/create/', views.get_url),
    path('ranch/web/site/index/', views.get_url),


    # path("", include("home.urls", namespace="home")),
    # path('news/', include('news.urls', namespace="news")),

    #news
    path("news/", NewsView.news_view, name="news"),
    path("news/<int:cat_id>/", NewsView.news_view, name="news_cat"),
    path("detail/<int:cat_id>/", NewsView.new_detail, name="new_detail"),
    # path('generate_word_document/', NewsView.generate_word_document, name='generate_word_document'),

    

    # Tashqi
    path('translation/', include('translation_manager.urls')),

    path('api/', include('apps.home.urls', namespace="home"))
]

if DEBUG:
    # See https://docs.djangoproject.com/en/4.1/howto/static-files/#serving-files
    # https://stackoverflow.com/questions/61770551/how-to-run-django-with-uvicorn-webserver-uploaded-by-a-user-during-development
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),

    path("set_language/<str:language>/", HomwViews.set_language, name="set-language"),
    ]
