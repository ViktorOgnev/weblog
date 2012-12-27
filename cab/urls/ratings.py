from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<snippet_id>\d+)/?$', 'cab.views.ratings.rate',
            name='cab_snippet_rate'),
    )

    