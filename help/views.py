from django.shortcuts import render

def home_view(request):
	return render(request, 'help/home_view.html')


def articles_view(request):
	return render(request, 'help/articles_view.html')
