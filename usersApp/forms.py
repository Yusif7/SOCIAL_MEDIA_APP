from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    # widget=forms.PasswordInput указывает, что это поле формы должно отображаться как поле для ввода пароля,
    # символы, будут скрыты (заменены точками или звездочками)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')

    # check password equality
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password != password2:
            # raise используется для генерации исключения
            raise forms.ValidationError('Passwords do not match')
        return password2


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        # We can change this fields
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        # We can change this fields
        fields = ('photo',)
