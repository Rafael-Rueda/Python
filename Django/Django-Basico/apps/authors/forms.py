from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget.attrs['placeholder'] = 'Type your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat your password'
        self.fields['username'].widget.attrs['placeholder'] = 'Type your username'
        self.fields['email'].widget.attrs['placeholder'] = 'Type your email'

    password = forms.CharField(required=True, widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(), label='Repeat password')

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        data = super().clean()
        password = data.get('password', '')
        password2 = data.get('password2', '')

        if password and password2:
            if password != password2:
                raise forms.ValidationError({
                    'password': 'Passwords must be equal.',
                    'password2': 'Passwords must be equal.',
                })

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Type your username.'
        self.fields['password'].widget.attrs['placeholder'] = 'Type your password.'
        
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(required=True, widget=forms.PasswordInput(), label='Password')

class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget.attrs['placeholder'] = 'Type your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat your password'
        self.fields['username'].widget.attrs['placeholder'] = 'Type your username'
        self.fields['email'].widget.attrs['placeholder'] = 'Type your email'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Type your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Type your last name'

    password = forms.CharField(required=True, widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(), label='Repeat password')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        data = super().clean()
        password = data.get('password', '')
        password2 = data.get('password2', '')

        if password and password2:
            if password != password2:
                raise forms.ValidationError({
                    'password': 'Passwords must be equal.',
                    'password2': 'Passwords must be equal.',
                })