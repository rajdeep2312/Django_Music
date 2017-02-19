from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    url(r'^albums/$', views.albums, name='albums'),
    url(r'^punjabi/$', views.punjabi, name='punjabi'),
    url(r'^english/$', views.english, name='english'),
    url(r'^hindi/$', views.hindi, name='hindi'),
    url(r'^edm/$', views.edm, name='edm'),
    url(r'^devotional/$', views.devotional, name='devotional'),
    url(r'^workout/$', views.workout, name='workout'),

]
