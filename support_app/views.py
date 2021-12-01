
from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    userform = UserForm()
    return render(request, "index.html",
                  {'form': userform})
