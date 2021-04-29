from django.shortcuts import render
from .forms import PostModelForm
# Create your views here.

def index(req):
    return render(req, 'index.html')

def newpost(req):
    if req.method == "POST":
        post = req.POST or None
        form = PostModelForm(post)
        if form.is_valid():
            form.save()        