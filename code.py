from django.db import models
from django.http import HttpReponse
def view(request):
    return HttpResponse('hello python')
