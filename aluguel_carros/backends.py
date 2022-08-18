from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


from django.contrib.auth.backends import ModelBackend

class SettingsBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):   
        usuario = request.user
        try:
            user = User.objects.get(username=usuario)
        except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
            user = User(username=usuario)
            user.is_staff = True
            user.is_superuser = True
            user.save()
        return user

    def get_user(self, user_id):
        return User.objects.get(pk=user_id)
        