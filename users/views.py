from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Welcome {username}, you are now registered! Please log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Profile Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }


    return render(request, 'users/profile.html', context)

    ## My code
    # if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST or None,
    #                             instance=request.user)
    #     p_form = ProfileUpdateForm(request.POST or None,
    #                                instance=request.user.profile)
    #
    #     user = request.user
    #
    #     context = {
    #         'u_form': u_form,
    #         'p_form': p_form
    #     }
    #     if u_form.is_valid() and p_form.is_valid():
    #         user.username = request.POST['username']
    #         user.email = request.POST['email']
    #         user.profile.image = request.POST['image']
    #         user.save()
    #     else:
    #         return render(request, 'users/profile.html', context)
    # else:
    #     u_form = UserUpdateForm()
    #     p_form = ProfileUpdateForm()
    #     context = {
    #         'u_form': u_form,
    #         'p_form': p_form
    #     }
    #     return render(request, 'users/profile.html', context)


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, f'Welcome back {username}.')
        return redirect('blog-home')
    else:
        messages.error(request, f'Sorry, login failed. Please try again.')
    return render(request, 'users/login.html')


def logout(request):
    logout(request)
    messages.success(request, f'You are now logged out.')
    return redirect('blog-home')
