from django.urls import path

from . import views

app_name = 'authentication'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile'),
    path('profileEdit/', views.profileEdit, name='profileEdit'),
    path('publish/', views.publish, name='publish'),
]
