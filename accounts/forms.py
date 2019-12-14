from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control', 
                'placeholder': 'Enter your username here'
                }
            ),
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
            'class': 'form-control',
            'placeholder': 'Enter your password here',
            }
        ),
    )
    class Meta:
        error_messages = {
            'username':{
                'invalid': 'What is this!?'
            }
        }


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, label='Password', 
    help_text='Required, please contain at least 8 character', 
    widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Password from numbers and letters of the Latin alphabet'}))
    password2 = forms.CharField(max_length=16, label='Password confirm',
    help_text='Please enter the same password as before', 
    widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 'placeholder': 'Password confirm'}))
    email = forms.EmailField(required=True, help_text='Please provide valid email', widget=forms.EmailInput(
        attrs={
            'class': 'form-control', 'placeholder': 'Input your email'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

        widgets = {
            'username':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Input your username',
                }
            ),
        }


class EditProfileForm(UserChangeForm):
    class Meta:
        model   = User
        fields  = [
            'email',
            'first_name',
            'last_name',
            'password',
        ]

        widgets = {
            'email':forms.TextInput(
                attrs = {
                    'class':'form-control',
                }
            ),
            'first_name':forms.TextInput(
                attrs = {
                    'class':'form-control',
                }
            ),
            'last_name':forms.TextInput(
                attrs = {
                    'class':'form-control',
                }
            ),
        }

class EditPasswordForm(PasswordChangeForm):
    # old_password = forms.CharField(
    #     widget = forms.PasswordInput(
    #         attrs = {
    #             'class': 'form-control', 
    #             }
    #         ),
    # )
    # new_password1 = forms.CharField(
    #     widget = forms.PasswordInput(
    #         attrs = {
    #         'class': 'form-control',
    #         }
    #     ),
    # )
    class Meta:
        model   = User
        fields  = [
            'old_password',
            'new_password1',
            'new_password2',
        ]

        widgets = {
            'old_password':forms.PasswordInput(
                attrs = {
                    'class':'form-control',
                }
            ),
            'new_password1':forms.PasswordInput(
                attrs = {
                    'class':'form-control',
                }
            ),
            'new_password2':forms.PasswordInput(
                attrs = {
                    'class':'form-control',
                }
            ),
        }