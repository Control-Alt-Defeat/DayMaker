from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from users.forms import CustomUserCreationForm, CustomUserChangeForm
# Create your views here.

def signup(request):
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
    return render(request, 'signup.html',{'form': form})
def account_details(request):
    return render(request,'accountDetails.html')

def account_edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('../accountDetails')
        else:
            print(form.errors)
            return render(request, "accountEdit.html", {'form': form})

    else:
        user = request.user
        form = CustomUserChangeForm(initial={'username': user.username,'first_name':user.first_name,'last_name': user.last_name,'email': user.email})
        
        return render(request, 'accountEdit.html',{'form': form})

            
            
    
