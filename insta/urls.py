from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.instagram,name = 'instagram'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^search/', views.search_results, name='search_results'),   
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)