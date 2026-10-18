from decimal import Decimal
from typing import Any

from django import forms
from django.core.exceptions import ValidationError

from reviews.models import Review
from templatesexercise.mixins import DisabledFormMixin


class ReviewBaseForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

    def clean_rating(self) -> Decimal:
        rating = self.cleaned_data['rating']

        if not 0 < rating < 5:
            raise ValidationError("Rating must be between 0 and 5")

        return rating

    def clean(self) -> dict[str, Any] | None:
        cleaned_data = super().clean()
        if cleaned_data.get('is_spoiler') and not cleaned_data.get('body'):
            self.add_error('body', 'Making as spoiler must include a body')

        return cleaned_data


class ReviewCreateForm(ReviewBaseForm):
    ...

class ReviewEditForm(ReviewBaseForm):
    ...

class ReviewDeleteForm(DisabledFormMixin ,ReviewBaseForm):
    ...