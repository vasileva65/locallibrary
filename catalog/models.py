from django.db import models

class Genre(models.Model):
    
    name = models.CharField(max_length=200, help_text="Enter a book genre")

    def __str__(self):
        return self.name
    
class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character')
    genre = models.ManyToManyField(Genre, help_text="Select a genre fo this book")