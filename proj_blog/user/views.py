from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import login as login_views
from django.contrib.auth import logout as logout_views
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please login to continue')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UpdateRegisterForm(request.POST,instance = request.user)
        p_form = ProfileRegisterForm(request.POST,request.FILES,instance=request.user.profile)
        u_form.save()
        p_form.save()
        messages.success(request, f'Your information has been saved')
        return redirect(profile)
    else:
        u_form = UpdateRegisterForm(instance=request.user)
        p_form = ProfileRegisterForm(request.FILES, instance=request.user.profile)

    context ={
        'u_form': u_form,
        'p_form':p_form
    }

    return render(request,'user/profile.html',context)