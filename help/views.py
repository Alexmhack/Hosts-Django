from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
	return HttpResponse("<h1>Help Home Page lives here</h1>")


def articles_view(request):
	return HttpResponse("<h1>Help Articles Page lives here</h1>")
