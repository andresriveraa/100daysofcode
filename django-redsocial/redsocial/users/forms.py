from django import forms


class ProfileForm(forms.Form):
    wePage = forms.URLField(max_length=200, required=False)
    interest = forms.CharField(max_length=500, required=True)
    image = forms.ImageField()
