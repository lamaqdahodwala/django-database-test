from django.shortcuts import render, redirect
from .forms import PostModelForm
from django.http import HttpResponse

def index(req):
    return render(req, 'index.html')

def newpost(req):
    if req.method == "POST":
        post = req.POST or None
        form = PostModelForm(post)
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponse("Your post was submitted")
        return HttpResponse("Your post is invalid")
    return redirect(req, 'index.html')
