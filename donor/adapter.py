from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):

    def get_signup_redirect_url(self, request):
        path = "/donor/profile"
        return path