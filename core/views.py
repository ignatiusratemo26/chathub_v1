from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import SignUpForm

def frontpage(request):
    return render(request, 'core/index.html')

#creating the sign up view
def signup(request):
    #to check if form is submitted
    if request.method == 'POST':
        #new instance of the form
        form = SignUpForm(request.POST)
        #to check if credentials are okay
        if form.is_valid():
            #save user if credentials are okay
            user = form.save()
            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

