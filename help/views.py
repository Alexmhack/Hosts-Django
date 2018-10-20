from django.shortcuts import render

def home_view(request):
	return render(request, 'home_view.html')


def articles_view(request):
	return render(request, 'articles_view.html')
