from django.conf.urls import patterns, include, url
from coltrane.models import Entry
from coltrane.feeds import LatestEntriesFeed, CategoryFeed
from django.contrib import admin

admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^signup/', 'signup.views.signup', name='auth_signup'),
    url(r'^login/', 'django.contrib.auth.views.login', name='auth_login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', name='auth_logout'),
    url(r'^admin/?', include(admin.site.urls)),
    url(r'^weblog', include('coltrane.urls')),
    url(r'^weblog', include('cab.urls.cab_urls')),
    
    url(r'^feeds/entries/?$', LatestEntriesFeed(), name='latest_entry_feeds'),
    url(r'^feeds/(?P<slug>\w+)/?$', CategoryFeed(), name='category_feeds'),
    
                                                       
    url(r'^search/?$', 'search.views.search'),
    )                                         
    
    
    
    
    

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*)$', 'flatpage'),
    )
    
    