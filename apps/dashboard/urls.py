from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('dashboard.views',
    url(r'^ajax/sentiment/?', 'sentiment'),
    url(r'^ajax/trends/?', 'trends'),
)
