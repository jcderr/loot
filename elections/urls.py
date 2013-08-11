from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^(?P<hoard>.*)/', 'elections.views.results', name='results'),
    url(r'^$', 'elections.views.election', name='election'),
)
