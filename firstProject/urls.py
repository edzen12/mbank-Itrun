from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from news.views import homepage, mkassaPage, installmentPage, Mjunior

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('mkassaPage/', mkassaPage, name='mkassaPage'),
    path('Mjunior/', Mjunior, name='junior'),
    path('installmentPage/', installmentPage, name='installmentPage'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
