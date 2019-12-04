from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from users.forms import CustomUserCreationForm, CustomUserChangeForm
# Create your views here.

def signup(request):
    template_name = 'account/signup.html'
    context = {}
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('planner:plan_index')
    else:
        form = CustomUserCreationForm()
    
    context['form'] = form
    context['title'] = 'Sign Up'
    context['button'] = 'Sign Up'
    context['back_url'] = 'login'
    return render(request, template_name, context)

def account_details(request):
    return render(request,'account/accountDetails.html')

def account_edit(request):
    template_name = 'account/signup.html'
    context = {}
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account_details')
        else:
            print(form.errors)
    else:
        user = request.user
        form = CustomUserChangeForm(initial={'username': user.username,'first_name':user.first_name,'last_name': user.last_name,'email': user.email})

    context['form'] = form
    context['title'] = 'Edit Account'
    context['button'] = 'Save Account'
    context['back_url'] = 'account_details'

    return render(request, template_name, context)
