from django.conf.urls import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^welcome/', include('welcome.urls')),
    url(r'^sgce/accounts/', include('accounts.urls')),
    url(r'^sgce/registration/', include('accounts.urls')),
    url(r'^sgce/', include('ced_main.urls')),
    url(r'^sgce/accounts/', include('registration.backends.default.urls')),
    url(r'^sgce/accounts/', include('django.contrib.auth.urls')),
    url(r'^sgce/grsgmap/', include('grsgmap.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('welcome.urls'))
]