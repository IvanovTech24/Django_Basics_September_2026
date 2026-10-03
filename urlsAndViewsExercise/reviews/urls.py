from django.urls import re_path

from reviews.views import review_by_year

urlpatterns = [
    re_path(r'^(?P<year>20\d{2})/', review_by_year, name='review-by-year')
]