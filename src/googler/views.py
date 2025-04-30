from django.shortcuts import render
from django.http import HttpResponse
from . import oauth
# Create your views here.


def google_login_redirect_view(request):
    google_auth_url = oauth.generate_auth_url()
    return HttpResponse(google_auth_url)


def google_login_callback_view(request):
    return HttpResponse( 'google_login_callback.html')

