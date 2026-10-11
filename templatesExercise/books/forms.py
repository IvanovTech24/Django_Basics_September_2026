from django import forms
from books.models import Book, Tag
from templatesexercise.mixins import DisabledFormMixin


# created for comparison with forms.ModelForm
# class BookFormBasic(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#         # widget=forms.Textarea(
#         #     attrs={
#         #         'placeholder': 'e.g. Done'
#         #     }
#         # )
#     )
#     price = forms.DecimalField(
#         max_digits=6,
#         decimal_places=2,
#     )
#     isbn = forms.CharField(
#         max_length=12,
#     ),

class BookBaseForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    # field_order = [
    #     'isbn',
    #     'price',
    #     'title'
    # ]

    class Meta:
        model = Book
        exclude = ['slug']

class BookCreateForm(BookBaseForm):
    pass

class BookEditForm(BookBaseForm):
    pass

class BookDeleteForm(DisabledFormMixin, BookBaseForm):
    pass

class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
    )

