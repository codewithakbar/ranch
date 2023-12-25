from django.urls import include, path


from apps.core.web import views

urlpatterns = [
    path("", views.SimpleView.as_view()),
    # path("core/", include("apps.core.web.urls"))
]


