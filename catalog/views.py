from django.shortcuts import render
from .models import Author, Book ,BookInstance ,Genre
from django.views import generic
# Create your views here.
def index(request):
    """view function for the home page of the site"""
    num_books =  Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()
    num_genres=Genre.objects.count()
    num_books_containing_the= Book.objects.filter(title__icontains="The").count()
    context={
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors,
        'num_books_containing_the':num_books_containing_the,
        'num_genres':num_genres
    }
    return render(request,'index.html',context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    
class AuthorDetailView(generic.DetailView):
    model = Author
    
