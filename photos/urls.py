from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url('^$',views.home,name = 'welcome-page'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^category/(\w+)', views.get_category,name='get_category'),
    url(r'^location/(\w+)', views.get_location,name='get_location'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)