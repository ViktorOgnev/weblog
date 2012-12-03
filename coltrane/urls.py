from django.conf.urls.defaults import *
from coltrane.models import Category, Entry, Link
from django.views.generic import dates
from django.views.generic.list import ListView
from tagging.models import Tag

entry_view_params = {'queryset': Entry.live.all(), 'date_field': "pub_date"}

urlpatterns = patterns('',
    
    # Entry URLs
    
    url(r'^/?$',
            dates.ArchiveIndexView.as_view(**entry_view_params),
            name='coltrane_entry_archive_index'),
    url(r'^(?P<year>\d{4})/?$',
            dates.YearArchiveView.as_view(**entry_view_params),
            name='coltrane_entry_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/?$',
            dates.MonthArchiveView.as_view(**entry_view_params),
            name='coltrane_entry_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/?$',
            dates.DayArchiveView.as_view(**entry_view_params),
            name='coltrane_entry_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/?$', 
            dates.DateDetailView.as_view(**entry_view_params),
            name='coltrane_entry_detail'),
    
    # Link URLs
    
    url(r'^links/?$',
            dates.ArchiveIndexView.as_view(model=Link, date_field="pub_date"),
            name='coltrane_link_archive_index'),
    url(r'^links/(?P<year>\d{4})/?$',
            dates.YearArchiveView.as_view(model=Link, date_field="pub_date"),
            name='coltrane_link_archive_year'),
    url(r'^links/(?P<year>\d{4})/(?P<month>\w{3})/?$',
            dates.MonthArchiveView.as_view(model=Link, date_field="pub_date"),
            name='coltrane_link_archive_month'),
    url(r'^links/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/?$',
            dates.DayArchiveView.as_view(model=Link, date_field="pub_date"),
            name='coltrane_link_archive_day'),
    url(r'^links/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/?$', 
            dates.DateDetailView.as_view(model=Link, date_field="pub_date"),
            name='coltrane_link_detail'),
    
    # Category URLs
    
    url(r'^categories/$', ListView.as_view(model=Category), name='category_list'),
    
    url(r'^categories/(?P<slug>[-\w]+)/$', 'coltrane.views.category_detail'),
    
    # Tag URLs
    
    url(r'^tags/$', ListView.as_view(model=Tag)),
    
    url(r'^tags/entries/(?P<tag>[-\w]+)/$','tagging.views.tagged_object_list',
            { 'queryset_or_model': Entry.live.all(),
              'template_name': 'coltrane/entries_by_tag.html' }),
    url(r'^tags/links/(?P<tag>[-\w]+)/$', 'tagging.views.tagged_object_list',
            { 'queryset_or_model': Link,
              'template_name': 'coltrane/links_by_tag.html' }),

    )