from django.contrib import admin
from django.urls import include, path

urlpatterns = [
        path("", include("base.urls")),
        path("admin/", admin.site.urls),
        ]
# from django.conf import settings
# from django.conf.urls import patterns, include, url
# from django.conf.urls.static import static

# from django.contrib import admin

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'idfinder_django.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^app/', include("idfinder_app.urls", namespace="app")),
#     url(r'^admin/', include(admin.site.urls)),
# ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
