from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70,
                                            widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=2, max_length=2)
    last_name = forms.CharField(min_length=2, max_length=2)
    email = forms.CharField(min_length=6, max_length=70,
                            widget=forms.EmailInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username).exist
        if username_taken:
            raise forms.ValidationError('User is already exist')
        return username

    def clean(self):
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password di ni match')
        return data


class ProfileForm(forms.Form):
    wePage = forms.URLField(max_length=200, required=False)
    interest = forms.CharField(max_length=100, required=True)
    image = forms.ImageField(required=False)
