from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^popular/', include('cab.urls.popular')),
    url(r'^snippet/', include('cab.urls.snippets')),
    url(r'^language/', include('cab.urls.languages')),
    url(r'^bookmark/', include('cab.urls.bookmarks')),
    url(r'^rating/', include('cab.urls.ratings')),
    )