# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from books.models import Book
from django.shortcuts import render, get_object_or_404

def index(request):
    latest_book_list = Book.objects.order_by('-pub_year')[:5]
    template = loader.get_template('books/index.html')
    context = RequestContext(request, {
        'latest_book_list': latest_book_list,
    })
    return HttpResponse(template.render(context))

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/detail.html', {'book': book})