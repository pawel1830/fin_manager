
from django.conf.urls import url,include
from django.contrib import admin
import fin_manager.urls

# ... the rest of your URLconf here ...


urlpatterns = [
    url(r'^', include(fin_manager.urls)),
    url(r'^admin/', admin.site.urls),
]
#urlpatterns += staticfiles_urlpatterns()
