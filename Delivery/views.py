from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import DeliverguyProfileInfoForm,signupform
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import DelProfile

def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if DelProfile.objects.filter(user=user).exists():
                return HttpResponse('u have logged in and u have a profile')
            else:
                return redirect('http://127.0.0.1:8000/customer/profile')
        else:
            return render(request, 'Delivery/index.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request,'Delivery/index.html',{'form': form})


def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('http://127.0.0.1:8000/')
        else:
            return render(request, 'Delivery/signup.html', {'form': form,})
    else:
        form = signupform()
    return render(request, 'Delivery/signup.html', {'form': form,})


def profilepage(request):
    if request.method == 'POST':
        profile_form = DeliverguyProfileInfoForm(data=request.POST)
        # print(form)
        if  profile_form.is_valid()  :
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('http://127.0.0.1:8000/delivery/')
        else:
            return render(request, 'Delivery/profile.html', {'Profile_form': profile_form})
    else:
        profile_form = DeliverguyProfileInfoForm()
    return render(request, 'Delivery/profile.html', {'Profile_form': profile_form})
