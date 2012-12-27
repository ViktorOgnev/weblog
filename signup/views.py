from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def signup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
    else:
        form = SignupForm()
    return render_to_response('signup.html', {'form':form})
    
    
    
