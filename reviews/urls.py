from django.urls import path
from . import views
app_name = 'reviews'




urlpatterns = [
    path('<int:book_id>/add', views.AddReview.as_view(), name='add-book-review'),
    path('<int:book_id>/<int:review_id>/edit', views.EditReview.as_view(), name='edit-book-review'),
    path('<int:book_id>/<int:review_id>/publish', views.PublishReview.as_view(), name='publish-book-review'),
    path('list', views.ListReviews.as_view(), name='list-reviews'),
]