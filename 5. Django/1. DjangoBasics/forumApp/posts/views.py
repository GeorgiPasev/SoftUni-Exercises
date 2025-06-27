from django.shortcuts import render
from django.utils import timezone

from posts.forms import MyForm, PostForm


# Create your views here.

def index(request):
    form = PostForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()

    context = {
        "form": form,
    }
    return render(request, 'index.html', context)

def dashboard(request):
    context = {
        "posts": [
            {
                "title": "how to work with templates?",
                "author": "G.P.",
                "content": "Hey how can I work with templates in Django?balb lablab lablablalblabl ablablalbl ablablablalbalbal",
                "created_at": timezone.now(),
            },
            {
                "title": "was lecture good?",
                "author": "Anonymous",
                "content": "Should I watch it?",
                "created_at": timezone.now(),
            },
            {
                "title": "what is next lecture?",
                "author": "",
                "content": "Hey guys I have no idea, pls answer!!!",
                "created_at": timezone.now(),
            },
        ]
    }
    return render(request, 'base.html', context)

