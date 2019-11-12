from django.shortcuts import render
from projects.models import Project
from blog.models import Post, Comment


# Create your views here.

def home_index(request):
    projects = Project.objects.all()
    posts = Post.objects.all().order_by('-created_on')

    context = {
        'projects': projects,
        "posts": posts,
    }
    return render(request, 'home_index.html', context)

# def home_index(request):
#     return render(request, 'home_index.html')
