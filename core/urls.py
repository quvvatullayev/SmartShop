from django.contrib import admin
from django.urls import path,include,reverse
from django.conf import settings
from django.conf.urls.static import static

url_name = 'base'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('user/', include('user.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls',success_url = reverse('product:categorys') ), name='dj_user'),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
