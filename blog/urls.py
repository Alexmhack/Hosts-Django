from django.urls import path

from .views import blog_home, blog_list

urlpatterns = [
	path('', blog_home, name='home'),
	path('list/', blog_list, name='list'),
]
