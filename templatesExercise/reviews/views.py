from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from books.forms import BookDeleteForm
from reviews.forms import ReviewCreateForm, ReviewEditForm
from reviews.models import Review

DEFAULT_REVIEWS_COUNT = 5

def recent_reviews(request: HttpRequest) -> HttpResponse:
    reviews_count = int(request.GET.get('count', DEFAULT_REVIEWS_COUNT)) # reviews/?count=3

    reviews = Review.objects.select_related('book')[:reviews_count]

    context = {
        'reviews': reviews,
        'page_title': 'Recent Reviews',
    }

    return render(request, 'reviews/list.html', context)


def review_details(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(Review.objects.select_related('book'), pk=pk)

    context = {
        'review': review,
        'page_title': f'{review.author}\'s review on {review.book.title}'
    }

    return render(request, 'reviews/detail.html', context)


def review_create(request: HttpRequest) -> HttpResponse:
    form = ReviewCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('books:list')

    context = {
        'form': form,
        'page_title': 'Create Review'
    }

    return render(request, 'reviews/create.html', context)

def review_edit(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(
        Review.objects.select_related('book'),
        pk=pk,
    )
    form = ReviewEditForm(request.POST or None, instance=review)

    if form.is_valid():
        form.save()
        return redirect('books:list')

    context = {
        'form': form,
        'page_title': 'Edit Review'
    }

    return render(request, 'reviews/edit.html', context)


def review_delete(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(
        Review.objects.select_related('book'),
        pk=pk,
    )
    form = BookDeleteForm(isinstance=review)

    if request.method == 'POST':
        review.delete()
        return redirect('books:list')

    context = {
        'form': form,
        'page_title': 'Delete Review',
    }

    return render(request, 'reviews/delete.html', context)
















