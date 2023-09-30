from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views

url_name = 'base'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('user/', include('user.urls'), name='user'),
    path('login/', auth_views.LoginView.as_view(), name='my_custom_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='my_custom_logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
