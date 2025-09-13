from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import post
# Create your views here.

# home page
def home(request):
    # person.objects.create(name="Alice", age=25, school="Greenwood High")
    p = post.objects.all()
    return render(request, 'index.html', {'p' : p})


# indidual posts
def pos(request, pk):
    ps = post.objects.get(id=pk)
    return render(request, 'post.html', {'p' : ps})