from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('user/', include('user.urls')),
    path('auth/', include('rest_framework.urls'), name = 'aouth')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
