from django.urls import path

from . import views

app_name = 'web_content'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('favorites/', views.favorites, name='favorites'),
    path('about/', views.about, name='about'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
]
