from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from signup.models import SignupForm
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request)
            
    else:
        form = SignupForm()
    c =  {'form': form} 
    c.update(csrf(request))
    return render_to_response('registration/signup.html', c,
                               context_instance=RequestContext(request))

# def site_login(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(username=username, password=password)
    # if user is not None:
        # if user.is_active:
            # login(request, user)
            # return HttpResponseRedirect('signup.views.login')
        # else:
            # # Return a 'disabled account' error message
    # else:
        # # Return an 'invalid login' error message.