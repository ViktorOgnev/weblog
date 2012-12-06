from django.conf.urls import patterns, include, url
from coltrane.models import Entry


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
    url(r'^admin/?', include(admin.site.urls)),
    url(r'^weblog', include('coltrane.urls')),
    
    url(r'^search/?$', 'search.views.search'),
    )                                         
    
    
    
    
    

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*)$', 'flatpage'),
    )
    
    