from django.contrib import admin
from django.urls import path, include  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('polls/', include('polls.urls')),  
    path('admin/', admin.site.urls),
]
if settings.DEBUG: 
    import debug_toolbar
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
