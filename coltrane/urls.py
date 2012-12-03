from django.conf.urls.defaults import *
from coltrane.models import Entry
from django.views.generic import dates

urlpatterns = patterns('',
    url(r'^/?$',
            dates.ArchiveIndexView.as_view(model=Entry, date_field="pub_date"),
            name='coltrane_entry_archive_index'),
    url(r'^(?P<year>\d{4})/?$',
            dates.YearArchiveView.as_view(model=Entry, date_field="pub_date"),
            name='coltrane_entry_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/?$',
            dates.MonthArchiveView.as_view(model=Entry, date_field="pub_date"),
            name='coltrane_entry_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/?$',
            dates.DayArchiveView.as_view(model=Entry, date_field="pub_date"),
            name='coltrane_entry_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/?$', 
              dates.DateDetailView.as_view(model=Entry, date_field="pub_date"),
              name='coltrane_entry_detail'),
    
    )