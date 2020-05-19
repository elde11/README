from django.urls import path

from . import views


app_name = 'books'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('authors/', views.AuthorIndexView.as_view(), name='list-authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-details'),
    path('books/', views.BookIndexView.as_view(), name='list-books'),
    path('categories/', views.CategoryIndexView.as_view(), name='list-categories'),
    path('categories/<int:pk>', views.CategoryDetailView.as_view(), name='category-details'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-details'),
]