from django.shortcuts import render
from .models import Poem

def index(request):
    return render(request, 'myapp5/index.html')

def get_poems(request):
    context = {'poems': Poem.objects.all()}
    return render(request, 'myapp5/get_poems.html', context)

def add_poem(request):
    if request.method == "GET":
        return render(request, 'myapp5/form.html')
    if request.method == "POST":
        data = request.POST
        Poem.objects.create(poem_name = data["poem_name"], poet_name  = data["poet_name"], age = data["age"], poem = data["poem"])
        return render(request, 'myapp5/done.html')