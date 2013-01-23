from cab.models import Language, Snippet
from django.views.generic.list import ListView
                               
def top_languages(request):
    return ListView.as_view(queryset=Language.objects.top_languages())(request, 
                              template_name='cab/top_languages.html',
                               paginate_by=20)
                       
def top_authors(request):
    return ListView.as_view(queryset=Snippet.objects.top_authors())(request,
                                           paginate_by=20)(request, 
                                           template_name='cab/top_authors.html',
                                           )
                       
def most_bookmarked(request):   
    return ListView.as_view(queryset=Snippet.objects.most_bookmarked())(request, 
                            template_name='cab/most_bookmarked.html',
                            paginate_by=20)
def top_rated(request):   
    return ListView.as_view(queryset=Snippet.objects.top_rated(),
                            template_name='cab/top_rated.html')(request, 
                            
                            paginate_by=20)