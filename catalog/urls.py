from django.urls import path

from catalog import views

urlpatterns = [
    path('', views.index,name='index'),
    path('books/',views.BookListView.as_view(),name="books"),
    # path('authors'),
    path('books/<pk>',views.BookDetailView.as_view(),name='book-detail')
    # path('author/<id>')
]