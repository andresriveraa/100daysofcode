from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse('hello world')


def login(request):
    numbers = request.GET['numbers']
    return HttpResponse(str(numbers))


def logout(request):
    name = request.GET['name']
    return HttpResponse(name)

