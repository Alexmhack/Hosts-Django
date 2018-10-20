from django.shortcuts import render
from django_hosts.resolvers import reverse

homepage_url = reverse('home', host='www')

def home_view(request):
	return render(request, 'help/home_view.html', {'homepage_url': homepage_url})


def articles_view(request):
	return render(request, 'help/articles_view.html', {'homepage_url': homepage_url})
