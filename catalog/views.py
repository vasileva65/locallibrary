from django.shortcuts import render

from catalog.models import Author, Book, BookInstance, Genre

from django.views import generic

def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count() 
    
    num_genres = Genre.objects.all().count()

    book = 'coraline'
    book_keyword_count = Book.objects.filter(title__icontains=book).count()
    genre = 'Детектив'
    genre_keyword_count = Genre.objects.filter(name__icontains=genre).count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genres': num_genres,
            'num_visits': num_visits,
            'book_keyword_count': book_keyword_count,
            'genre_keyword_count': genre_keyword_count,
        },
    )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)

        context['some_data'] = 'This is just some data'

        return context

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5

class AuthorDetailView(generic.DetailView):
    model = Author