from django.contrib import admin

from catalog.models import Author, Book, BookInstance, Genre, Language

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display=('last_name','first_name','date_of_birth','date_of_death')


class BookInstanceInline(admin.TabularInline) : 
  model=BookInstance
  list_filter=('status','due_back')
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display=('title','author','display_genre','language')
  inlines = [BookInstanceInline]



# admin.site.register(Book)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)