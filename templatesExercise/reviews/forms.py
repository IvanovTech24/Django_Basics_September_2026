from django import forms
from reviews.models import Review
from templatesexercise.mixins import DisabledFormMixin


class ReviewBaseForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewCreateForm(ReviewBaseForm):
    ...

class ReviewEditForm(ReviewBaseForm):
    ...

class ReviewDeleteForm(DisabledFormMixin ,ReviewBaseForm):
    ...