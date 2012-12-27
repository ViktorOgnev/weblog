from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'cab.views.bookmarks.user_bookmarks', name='cab_user_bookmarks'),
    url(r'^add/(?P<pk>\d+)/?$', 'cab.views.bookmarks.add_bookmark',
            name='cab_bookmark_add'),
    url(r'^delete/(?P<pk>\d+)/?$', 'cab.views.bookmarks.delete_bookmark',
            name='cab_bookmark_delete'),
    )