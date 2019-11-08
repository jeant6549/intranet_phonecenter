# Import
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# View
def hello(request):
	print("Bonjour")
	#return JsonResponse({'message':'Hello','price':19.6,})
	return HttpResponse("Hello World!")