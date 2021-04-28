from django.shortcuts import render

# Create your views here.

def index(req):
    return (req, 'index.html')