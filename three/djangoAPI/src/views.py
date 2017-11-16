from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(req):
    return render(req, 'index.html')