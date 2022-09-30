from django.shortcuts import render, redirect
from .models import Movies

# Create your views here.
def index(request):
    movies = Movies.objects.all()
    context = {
        "movies": movies,
    }

    return render(request, "movies/index.html", context)


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")

    Movies.objects.create(
        title=title,
        content=content,
    )

    context = {
        "title": title,
        "content": content,
    }
    return redirect("index")


def new(request):
    return render(request, "movies/new.html")


def update(request, pk):
    update = Movies.objects.get(id=pk)

    title = request.GET.get("title")
    content = request.GET.get("content")

    update.title = title
    update.content = content
    update.save()

    return redirect("index")


def edit(request, pk):
    edit = Movies.objects.get(id=pk)

    context = {
        "edit": edit,
    }

    return render(request, "movies/edit.html", context)


def detail(request, pk):
    detail = Movies.objects.get(id=pk)
    context = {
        "detail": detail,
    }
    return render(request, "movies/detail.html", context)


def delete(request, pk):
    Movies.objects.get(id=pk).delete()

    return redirect("index")
