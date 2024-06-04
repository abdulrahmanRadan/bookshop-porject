from django import forms
from .models import Book, Category


class BookForm(forms.ModelForm):
    class Meta:
        model  = Book
        fields = [
            'title',
            'author',
            'photo_book',
            'photo_author',
            'pages',
            'price',
            'retal_price_day',
            'retal_period',
            'status',
            'category'
        ]
    widgets = {
        'title': forms.TextInput(attrs = {'class':' form-control '}),
        'author': forms.TextInput(attrs={'class':'form-control'}),
        'photo_book': forms.TextInput(attrs={'class':'form-control'}),
        'photo_author': forms.TextInput(attrs={'class':'form-control'}),
        'pages': forms.TextInput(attrs={'class':'form-control'}),
        'price': forms.TextInput(attrs={'class':'form-control'}),
        'retal_price_day': forms.TextInput(attrs={'class':'form-control'}),
        'retal_period': forms.TextInput(attrs={'class':'form-control'}),
        'status': forms.Select(attrs={'class':'form-control'}),
        'category': forms.Select(attrs={'class':'form-control'}),
    }