from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, ProfileForm, UserEditForm
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {
        'form': form,
    })


@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST)
        profile = Profile.objects.get(user=request.user)
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            message = "Profile saved successfully!"
            profile_form = ProfileForm(instance=request.user.profile, data=request.POST)
            profile = Profile.objects.get(user=request.user)
            user_form = UserEditForm(instance=request.user, data=request.POST)
            return render(request, 'home/index.html', {
                'message': message,
            })
    else:
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST)
        profile = Profile.objects.get(user=request.user)
        user_form = UserEditForm(instance=request.user, data=request.POST)
        message =""

    return render(request, 'user/profile.html', {
        'profile_form': profile_form,
        'profile': profile,
        'user_form': user_form,
    })
