from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta: # для чего этот класс?
        model = User
        fields = ['username', 'password']