from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
import notifications.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('members.urls')),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
