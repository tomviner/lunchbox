from django.conf import settings
from django.contrib.auth.models import check_password
from django.contrib.auth import get_user_model


try:
    from django.contrib.auth import get_user_model
except ImportError:
    from django.contrib.auth.models import User
else:
    User = get_user_model()


class TrustingBackend(object):
    """
    No authentication, just log me in
    """
    def authenticate(self, username=None, password=None):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None