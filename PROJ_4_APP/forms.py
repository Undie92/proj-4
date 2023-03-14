from django import forms

class SignupForm(forms.Form):
    
    Username = forms.CharField(max_length=40, required=True, label='Desired Username')
    Password = forms.PasswordInput()
    Email = forms.EmailField()
        