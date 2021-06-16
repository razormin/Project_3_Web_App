from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect('learning_logs:index')

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.   
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user,password=request.POST['password1'])
            # Log the user in and then redirect to home page.
            login(request, authenticated_user)
            return redirect('learning_logs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def logout_view(request):
	"""Log the user out"""
	logout(request)
	return redirect('registration/logged_out.html')