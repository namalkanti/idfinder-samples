from django.urls import path

from . import views 

urlpatterns = [
        path("main", views.main, name="main"),
        path("index", views.IndexView.as_view(), name="index"),
        path("form", views.form, name="form"),
        ]
# from django.conf.urls import patterns, include, url

# from django.contrib import admin

# from . import views

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'idfinder_django.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r"^$", views.main, name="main"),
#     url(r"^index", views.IndexView.as_view(), name="index"),
#     url(r"^form/", views.form, name="form"),
#     url(r"^success/", views.success, name="success"),
#     url(r"^(?P<pk>[0-9]+)/$", views.DetailView.as_view(), name="detail"),
#     url(r"^(?P<card_id>[0-9]+)/found/", views.found, name="found"),
#     url(r"^(?P<card_id>[0-9]+)/correct", views.password_correct, name="password_correct"),
#     url(r"^(?P<card_id>[0-9]+)/incorrect", views.password_incorrect, name="password_incorrect"),
# )
