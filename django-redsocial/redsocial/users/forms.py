from django import forms


class ProfileForm(forms.Form):

    website = forms.URLField(max_length=200, required=True)
    interest = forms.CharField(max_length=500, required=False)
    image = forms.ImageField()