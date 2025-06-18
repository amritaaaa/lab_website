from django import forms

# creating a form

class LoginForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput())

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email_id = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput())


