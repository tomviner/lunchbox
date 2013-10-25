from django.contrib.auth import get_user_model

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
