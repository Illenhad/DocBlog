from datetime import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """
    Initial view of the Blog app.
    
    :param requests: This is the request object that is sent to the server
    :return: The index template file is being returned.
    """
    return render(request=request, template_name='blog/index.html', context={'date': datetime.now()})