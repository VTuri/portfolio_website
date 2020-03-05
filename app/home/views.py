from blog.models import Post
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from projects.models import Project


# Create your views here.

def home_index(request):
    projects = Project.objects.all()
    posts = Post.objects.all().order_by('-created_on')

    context = {
        'projects': projects,
        "posts": posts,
    }
    return render(request, 'home_index.html', context)


def handler404(request, exception, template_name="404.html"):
    response = render("404.html")
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
