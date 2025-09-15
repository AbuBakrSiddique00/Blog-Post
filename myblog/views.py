from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import post
# Create your views here.

# home page
def home(request):
    # person.objects.create(name="Alice", age=25, school="Greenwood High")
    if request.method == 'POST':
        # if request.POST['post_id']:
            px = request.POST['post_id']
            obs = post.objects.get(id=px)
            obs.delete()
            return redirect('/')
    
    else:
        p = post.objects.all()
        return render(request, 'index.html', {'p' : p})

# indidual posts
def pos(request, pk):
    ps = post.objects.get(id=pk)
    return render(request, 'post.html', {'p' : ps})

# Create new Post
def createPost(request):
    # print('post')
    if request.method == 'POST':
            title = request.POST['title']
            body = request.POST['body']
            p = post.objects.create(title=title, body=body, created_date=timezone.now())
            p.save()
            return redirect('/')
    else:
        return render(request, 'newPost.html')

# Edit Post
def editPost(request):
    if request.method == 'POST':
        if request.POST.get('post_id_e'):
            id = request.POST['post_id_e']
            p = post.objects.get(id=id)
            return render(request, 'edit.html', {'p' : p})
        else:
            title = request.POST['title']
            body = request.POST['body']
            p = post.objects.create(title=title, body=body, created_date=timezone.now())
            p.save()
            return redirect('/')
    else:
         return redirect('/')