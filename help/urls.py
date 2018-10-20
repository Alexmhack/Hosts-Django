from django.urls import path

from . import views

app_name = 'help'

urlpatterns = [
	path('', views.home_view, name='home'),
	path('articles/', views.articles_view, name='articles'),
]
