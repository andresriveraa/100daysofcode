from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def post(request):
    return render(request, 'post/feed.html', {'feed': ' hola mundo feed'})
