from django.shortcuts import render

# Create your views here.
def post(request):
    return render(request, 'post/feed.html', {'feed': 'feed'})
