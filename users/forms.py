from django import forms
from .models import  customuser
from  django.contrib.auth.forms import UserCreationForm,UserChangeForm


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'form-control', }), label='Password')
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'form-control', }),label='Confirm Password')
    class Meta(UserCreationForm.Meta):
        model = customuser
        fields = ('username','email','password1','password2','name','surname','age','photo')

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class UpdateUserForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = customuser
        fields = ('username','email','name','surname','age','bio','photo')

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }
