from django.views.generic.detail import  DetailView
#from django.shortcuts import get_object_or_404, render_to_response
from cab.models import Snippet

def snippet_detail(request, pk):
    return render_to_response('cab/snippet_detail.html', 
                             {'object' : Snippet.objects.get(pk=pk)})