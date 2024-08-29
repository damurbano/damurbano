from django.urls import path

from myapp import views

urlpatterns = [path("", views.index),
            path("hello/<str:username>",views.hello),
            path("about/", views.about)]
