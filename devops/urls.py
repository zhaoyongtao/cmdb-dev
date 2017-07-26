
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('account.urls', namespace='account')),
    url(r'^op/', include('op.urls', namespace='op')),
]
