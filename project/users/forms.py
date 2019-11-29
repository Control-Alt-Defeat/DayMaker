from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name','last_name','email')

class CustomUserChangeForm(UserChangeForm):
    def __init__(self,*args,**kwargs):
        super(CustomUserChangeForm,self).__init__(*args,**kwargs)
        del self.fields['password']
            
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name','last_name','email')
        

        
