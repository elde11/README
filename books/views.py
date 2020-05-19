from django.shortcuts import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin

from django.db.models import Avg, Count
from django.contrib.auth.mixins import AccessMixin
from reviews.forms import GradeForm
from .models import Author, Book, Category

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title': 'Strona główna',
    }

class AuthorIndexView(ListView):
    template_name = "books/list_authors.html" # renderowany szablon
    model = Author # queryset = Question.objects.all() 
    # zmiena z wynikami do szablonu
    extra_context = {                     # dodatkowe zmienne do szablonu
        'title': 'List of Author',
    }


class AuthorDetailView(DetailView):
    template_name = 'books/author_details.html'
    model = Author


class BookIndexView(ListView):
    template_name = "books/list_books.html" # renderowany szablon
    model = Book # queryset = Question.objects.all() 
     #skad brane obiekty do widoku
     # zmiena z wynikami do szablonu
    extra_context = {                     # dodatkowe zmienne do szablonu
        'title': 'List of Books',
    }

    
class CategoryIndexView(ListView):
    template_name = "books/list_categories.html" # renderowany szablon
    model = Category # queryset = Question.objects.all() 
     # zmiena z wynikami do szablonu
    extra_context = {                     # dodatkowe zmienne do szablonu
        'title': 'List of Category',
    }

class CategoryDetailView(DetailView):
    template_name = "books/category_details.html" # renderowany szablon
    model = Category # queryset = Question.objects.all() 
    context_object_name = 'category'
    extra_context = {                    
        'title': 'category',
    }


class BookDetailView(AccessMixin, SingleObjectMixin, FormView):
    template_name = "books/book_details.html" # renderowany szablon
    model = Book # queryset = Question.objects.all() 
    form_class = GradeForm

    def get_success_url(self):
        return reverse('books:book-details', kwargs={'pk': self.object.pk})

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = self.object
        self.grade = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = {
            'title': f'Book {self.object.title} by {self.object.author}',
            'avg_grades':self.object.grade_set.aggregate(
                average=Avg('grade'), count=Count('grade')
            ),
        }
        context.update(kwargs)
        return super().get_context_data(**context)
