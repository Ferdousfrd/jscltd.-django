from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    return render(request, "pages/index.html", {
        "title": 'Welcome to JSC ltd. and co.'
    })