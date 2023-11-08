from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def JamPandu(request):
    return HttpResponse ('Hi JamPandu how are you')

def JigelRani(request):
    return HttpResponse('Hello')