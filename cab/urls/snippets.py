from django.conf.urls.defaults import *
from django.views.generic.list import ListView
from django.views.generic.detail import  DetailView
from cab.models import Snippet


snippet_info = {'queryset': Snippet.objects.all()}

urlpatterns = patterns('', 
    url(r'^$', ListView.as_view(paginate_by=20, **snippet_info), 
            name='cab_snippet_list'),
    url(r'^(?P<pk>\d+)/?$', 'cab.views.snippets.snippet_detail',
            name='cab_snippet_detail'),
    url(r'^add/?$', 'cab.views.snippets.add_snippet', name='cab_snippet_add'),
    url(r'^edit/(?P<pk>\d+)/?$', 'cab.views.snippets.edit_snippet', name='cab_snippet_edit'),
    
    )
