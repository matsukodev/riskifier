from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^', include('riskifier.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
