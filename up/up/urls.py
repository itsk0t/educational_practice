from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls', namespace='auth')),
    path('doc/', include('documents.urls', namespace='doc')),
    path('applications/', include('applications.urls', namespace='appli')),
    path('account/', include('account.urls', namespace='account')),
    path('main/', include('main.urls', namespace='main')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
