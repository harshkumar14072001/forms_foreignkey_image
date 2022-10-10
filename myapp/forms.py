from .models import *
from django import forms
class author_form(forms.ModelForm):
    class Meta:
        model=author
        fields='__all__'

class book_form(forms.ModelForm):
    class Meta:
        model=books
        fields='__all__'