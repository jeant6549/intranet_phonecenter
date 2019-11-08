# Import
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# View
def hello_old(request):
	print("Bonjour")
	#return JsonResponse({'message':'Hello','price':19.6,})
	return HttpResponse("Hello World!")

def hello(request):
	return render(
		request,
		'users/hello.html',
		{
			'message': "Hello World!",
		}
	)