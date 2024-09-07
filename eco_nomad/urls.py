from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Import settings here
from django.conf.urls.static import static  # Import static here

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("blog.urls"), name="blog-urls"),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
