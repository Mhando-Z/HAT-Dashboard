
from django.contrib import admin
from django.urls import path, include
#
from django.conf import settings
from django.conf.urls.static import static
#


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hat-api/', include('homepage.urls')),
    path('hat-users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
]

# imp for what you want to achieve.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
