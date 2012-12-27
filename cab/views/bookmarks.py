from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from cab.models import Bookmark, Snippet
from django.views.generic.list import ListView
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

@csrf_protect
@login_required
def add_bookmark(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    try:
        Bookmark.objects.get(user__pk=request.user.id, snippet__pk=snippet.id)
    except Bookmark.DoesNotExist:
        bookmark = Bookmark.objects.create(user=request.user, snippet=snippet)
    return HttpResponseRedirect(snippet.get_absolute_url())

@csrf_protect    
@login_required    
def delete_bookmark(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        
        Bookmark.objects.filter(user__pk=request.user.id, 
                                snippet__pk=snippet.id).delete()
        return HttpResponseRedirect(snippet.get_absolute_url())
    else:
        return render_to_response('cab/confirm_bookmark_delete.html',
                                  {'snippet': snippet},
                                  context_instance=RequestContext(request))
@login_required                                        
def user_bookmarks(request):
    return ListView.as_view(queryset=Bookmark.objects.filter(
                            user__pk=request.user.id)
                            )(request, template_name='cab/user_bookmarks.html',
                              paginate_by=20)
                                                