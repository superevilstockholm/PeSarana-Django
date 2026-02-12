from django import forms

class SignUpForm(forms.Form):
    nisn = forms.CharField(max_length=10, required=True)
    dob = forms.DateField(required=True)
    email = forms.EmailField(required=True, max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, required=True, min_length=8, max_length=255)
