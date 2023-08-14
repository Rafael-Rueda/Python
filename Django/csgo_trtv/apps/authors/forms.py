from django import forms
from django.contrib.auth.models import User

from utils.form_addplaceholder import addp


class LoginForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        addp(self.fields.get('username'), 'Type your username here')
        addp(self.fields.get('password'), 'Type your password here')

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Repeat Password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        addp(self.fields.get('username'), 'Type your username here')
        addp(self.fields.get('email'), 'Type your email here')
        addp(self.fields.get('password'), 'Type your password here')
        addp(self.fields.get('password2'), 'Confirm your password here')

    def clean(self):
        data = super().clean()
        password = data.get('password')
        password2 = data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError({
                'password': 'Passwords must be equal',
                'password2': 'Passwords must be equal',
            })
    