from django.shortcuts import render

from catalog.models import Author, Book, BookInstance, Genre

from django.views import generic

def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count() 
    
    num_genres = Genre.objects.all().count()

    keyword = "word"  # Замените на свое ключевое слово
    num_books_with_keyword = Book.objects.filter(title__icontains=keyword).count()
    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genres': num_genres,
            'num_books_with_keyword': num_books_with_keyword,
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