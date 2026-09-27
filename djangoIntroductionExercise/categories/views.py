from django.shortcuts import render
from django.http import HttpResponse

from categories.models import Category


def list_categories(request) -> HttpResponse:
    categories = Category.objects.all()

    context = {
        "categories": categories
    }

    return render(request, 'categories/list_categories.html', context)
