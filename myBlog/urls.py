
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home

app_name = 'post'
app_name = 'users'
app_name = 'api'
app_name = 'two_factor'

urlpatterns = [
    path('', home, name='home'),
    path('post/', include('post.urls')),
    path("users/", include('users.urls')),
    path('api/v1/', include('api.urls')),

    # path('account/', include(('two_factor.urls'), namespace='two_factor')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT) 