from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.generic.detail import  DetailView
from django.contrib.auth.decorators import login_required
#from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404, render_to_response
from django.forms import ModelForm
from cab.models import Snippet
from django.template import RequestContext
from django.core.context_processors import csrf
#from cab.forms import AddSnippetForm


def snippet_detail(request, pk):
    return render_to_response('cab/snippet_detail.html', 
                             {'object' : Snippet.objects.get(pk=pk)},
                             context_instance=RequestContext(request))
#----------- a shorter version(no farms.py and AddSnippetForm) of add_snippet,
#----------- that uses ModelForm


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        exclude = ['author']
        
        
@login_required
#@csrf_protect        
def add_snippet(request):
        if request.method == 'POST':
            form = SnippetForm(data=request.POST)
            if form.is_valid():
                new_snippet = form.save(commit=False)
                new_snippet.author = request.user
                new_snippet.save()
                return HttpResponseRedirect(new_snippet.get_absolute_url())
        else:
            form = SnippetForm()
        c =  {'form': form, 'add' : True} 
        c.update(csrf(request))
        return render_to_response('cab/snippet_form.html', c,
                                  context_instance=RequestContext(request))
                             
                             
                             
#--------- a standard way to write add_snippet                             

# @login_required                             
# def add_snippet(request):
    # if request.method == 'POST':
        # form = AddSnippetForm(author=request.user, data=request.POST)
        # if form.is_valid():
            # new_snippet = form.save()
            # return HttpResponseRedirect(new_snippet.get_absolute_url())
        # else:
            # form = AddSnippetForm(author=request.user)
        # return render_to_response('cab/add_snippet.html', {'form':form})
        
@login_required       
def edit_snippet(request, snippet_id):  
    snippet = get_object_or_404(Snippet, pk=snipet_id)
    if request.user.id != snippet.author.id:
        return HttpResponseForbidden   
    if request.method == 'POST':
        form = SnippetForm(instance=snippet, data=request.POST)
        if form.is_valid:
            snippet = form.save()
            return HttpResponseRedirect(snippet.get_absolute_url)
        else:
            form = SnippetForm(instance=snippet)
        return render_to_response('cab/snippet_form.html',
                                  {'form': form,'add': False},
                                  context_instance=RequestContext(request))