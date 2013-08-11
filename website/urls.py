from django.conf.urls import patterns, include, url
from blog.views import post, listview


urlpatterns = patterns(
    '',
    url(r'^blog/(?P<character>.+)/(?P<year>\d+)/(?P<month>\d+)/(?P<slug>.+)/',
        'blog.views.post', name='post'),
    url(r'^blog/(?P<character>.+)/', 'blog.views.listview', name='listview'),
    url(r'^blog/$', 'blog.views.listview', name='listview'),
    url(r'^$', 'website.views.home', name='home'),
)
