from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_list_or_404
from reviews.models import Review


def review_by_year(request: HttpRequest, year: int) -> HttpResponse:
    reviews = get_list_or_404(Review, created_at__year=year)

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/reviews-by-year.html', context)


