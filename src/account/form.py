from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput, EmailInput
    

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': PasswordInput(),
        }


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = [
    		    'username', 
                'email', 
    		    'password', 
    	]
        widgets = {
            'password': PasswordInput(),
            'email' : EmailInput()
        }