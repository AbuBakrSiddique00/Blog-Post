from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import post, comment
# Create your views here.

# home page
def home(request):
    # person.objects.create(name="Alice", age=25, school="Greenwood High")
    if request.method == 'POST':  
        # delete post
        px = request.POST['post_id']
        obs = post.objects.get(id=px)
        obs.delete()
        return redirect('/')
    else:
        p = post.objects.all()
        return render(request, 'index.html', {'p' : p})

# indidual post and comment
def pos(request, pk):
    if request.method == 'POST':
        text = request.POST['text']
        ps = post.objects.get(id=pk)
        comment.objects.create(text=text, pOst=ps)
        # com = comment.objects.filter(pOst=ps)
        com = ps.comments.all()
        return render(request, 'post.html', {'p' : ps,'com' : com})
    else:
        ps = post.objects.get(id=pk)
        com = comment.objects.filter(pOst=ps)
        return render(request, 'post.html', {'p' : ps,'com' : com})

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
    # temo_id = request.POST.get('post_id_e')
    if request.method == 'POST':
        id = request.POST.get('post_id_e')
        p = post.objects.get(id=id)
        return render(request, 'edit.html', {'p' : p})
    else:
         return redirect('/')
    
# submit edited post
def submit(request, ps):
     if request.method == 'POST':
          p = post.objects.get(id=ps)
          title = request.POST['title']
          body = request.POST['body']
          p.title = title
          p.body = body
        #   p.created_date = 
          p.save()
          return redirect('/')
     else:
          return redirect('/')