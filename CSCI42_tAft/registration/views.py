from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect

@login_required
def home(request):
    # Assuming UserProfileModel has a OneToOneField with the built-in User model
    # Adjust this to your actual model structure
    return redirect('/userprofile/')

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("registration:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
