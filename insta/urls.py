from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.instagram,name = 'instagram'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^newprofile/', views.new_profile, name='new_profile'),
    url(r'^search/', views.search_user, name='search_user'),  
    url(r'^comment/(?P<image_id>\d+)', views.add_comment, name='comment'), 
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)