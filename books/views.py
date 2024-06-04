from django.shortcuts import render
from .models import *
from .forms import BookForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()



    context = {
        'books':Book.objects.all(),
        'category':Category.objects.all(),
        'form':BookForm(),
    }
    return render(request, 'pages/index.html', context)


def show(request):
    context = {
        'books':Book.objects.all(),
        'category':Category.objects.all(),
    }
    return render(request,'pages/books.html',context)