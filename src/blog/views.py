from django.http import HttpResponse

# Create your views here.
def index(requests):
    return HttpResponse('<h1>Blog</h1>')