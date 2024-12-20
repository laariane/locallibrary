import uuid

from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.urls import reverse


# Create your models here.

class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a book  genre (e.g. Science fiction,French poetry ..."
    )

    def __str__(self):
        """ Returns a string representation of the genre """
        return self.name

    def get_absolute_url(self):
        return reverse('genre-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message="A genre with that name already exists.",
            ),
        ]


class Book(models.Model):
    title = models.CharField(
        max_length=50,
        help_text="Enter the title for the book",
    )
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    summary = models.TextField(
        help_text="Enter the summary of the book ",
        max_length=1000
    )
    isbn = models.CharField('ISBN', max_length=13,
                            unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    genres = models.ManyToManyField(Genre, help_text="select a genre for this book")
    language = models.ForeignKey(
        'Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """ Returns a string representation of the book"""
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True,
                          help_text="Unique ID for this particular book")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m',
                              help_text='Book availability status')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name} {self.first_name} '

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


class Language(models.Model):
    language_name = models.CharField(max_length=50,unique=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('language_name'),
                name='language_case_insensitive_unique',
                violation_error_message="A Language with that name already exists",
            ),

        ]
        ordering = ['language_name']

    def __str__(self):
        return f'{self.language_name}'

    def get_absolute_url(self):
        return reverse('language-detail', args=[str(self.id)])
