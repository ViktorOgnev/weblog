from django.conf.urls.defaults import *
from django.views.generic.list import ListView
from cab.models import Language
from cab.views.languages import language_detail

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(paginate_by=20, queryset=Language.objects.all()),
                                                      name='cab_language_list'), 
    url(r'^(?P<slug>[-\+\w]+)/?$', language_detail, name='cab_language_detail'),
    )