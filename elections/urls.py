from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', 'elections.views.election', name='election'),
)
