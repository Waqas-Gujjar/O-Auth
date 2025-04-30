from django.urls import path
from . import views

urlpatterns = [
    path('google/login/', views.google_login_redirect_view, name='google_login_redirect'),
    path('google/callback/', views.google_login_callback_view, name='google_login_callback'),
]
