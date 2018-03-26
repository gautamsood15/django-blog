from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput())
    # password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password1')
        
        def save(self,commit=True):
            user = super(UserCreateForm,self).save(commit=False)
            user.email  = self.cleaned_data['email']
            user.username = self.cleaned_data['username']
            user.password1 = self.cleaned_data['password1']
           # user.password2 = self.cleaned_data['password2']
            
            if commit:
                user.save()
            return user