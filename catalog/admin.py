from django.contrib import admin

from catalog.models import Author, Book, BookInstance, Genre, Language

# Register your models here.
class BookInline(admin.TabularInline):
  model = Book
  extra=0
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display=('last_name','first_name','date_of_birth','date_of_death')
  inlines = [BookInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  list_display = ('book','due_back','status','id')
class BookInstanceInline(admin.TabularInline) : 
  model=BookInstance
  list_filter=('status','due_back')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display=('title','author','display_genre','language')
  inlines = [BookInstanceInline]
admin.site.register(Genre)
admin.site.register(Language)

