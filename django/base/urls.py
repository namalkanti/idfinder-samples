from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views 

urlpatterns = [
        path("main", views.main, name="main"),
        path("index", views.IndexView.as_view(), name="index"),
        path("form", views.form, name="form"),
        path("success", views.success, name="success"),
        path("<int:pk>", views.DetailView.as_view(), name="detail"),
        path("<int:card_id>/found", views.found, name="found"),
        path("<int:card_id>/correct", views.password_correct, name="password_correct"),
        path("<int:card_id>/incorrect", views.password_incorrect, name="password_incorrect"),
        ] 
