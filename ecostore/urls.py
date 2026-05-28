from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('catalogo/', include('catalogo.urls')),
    path('vendas/', include('vendas.urls')),
    path('feedback/', include('feedback.urls')),
    path('api/', include('api_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
