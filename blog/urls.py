from . import views
from django.urls import path
from django.conf import settings  # Import settings here
from django.conf.urls.static import static  # Import static here

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>/',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/',
         views.comment_delete, name='comment_delete'),
    path(
        'like/<slug:slug>/',
        views.post_like,
        name='post_like'),
    # Like functionality
]

# Use the += operator correctly to append static URLs to the existing
# urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
