from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.urls import reverse_lazy

from .models import Review
from books.models import Book

class AddReview(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'reviews/add.html'
    fields = ['title','content','grade']
    success_url = reverse_lazy('reviews:list-reviews')

    def get_context_data(self, **kwargs):
        context = {
            'title': f'Dodaj recenzję książki "{self.book}"',
        }
        context.update(kwargs)
        return super().get_context_data(**context)


    def get_book(self):
        book_id = self.kwargs.get('book_id')
        return get_object_or_404(Book, pk=book_id)

    def get(self, request, *args, **kwargs):
        self.book = self.get_book()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.book = self.get_book()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = self.object
        form.instance.state = 'draft'
        self.grade = form.save()
        return super().form_valid(form)


class EditReview(LoginRequiredMixin, UpdateView):
    pk_url_kwarg = 'review_id'
    template_name = 'reviews/edit.html'
    fields = ['title', 'content', 'grade']
    success_url = reverse_lazy('reviews:list-reviews')

    def get_context_data(self, **kwargs):
        context = {
            'title': f'Edytuj recenzję "{self.object.title}" książki "{self.object.book}"',
        }
        context.update(kwargs)
        return super().get_context_data(**context)

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user, state='draft')


    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = self.object.book
        form.instance.state = 'draft'
        return super().form_valid(form)

class PublishReview(View):
    def post(self, request, *args, **kwargs):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id, state='draft', user=request.user)
        review.state = 'in_moderation'
        review.save()
        return redirect('reviews:list-reviews')


class ListReviews(ListView):
    template_name = 'reviews/list.html'
    extra_context = {
        'title': 'Lista Twoich recenzji'
    }

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user).order_by('state', 'pub_date')