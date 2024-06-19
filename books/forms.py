from django import forms
from .models import Book, Category
from .models import City

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
    widgets = {
        'name': forms.TextInput(attrs = {'class':'form-control '}),
    }
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
            'total_rental',
            'status',
            'category'
        ]
        widgets = {
            'title': forms.TextInput(attrs = {'class':' form-control '}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'photo_book': forms.FileInput(attrs={'class':'form-control'}),
            'photo_author': forms.FileInput(attrs={'class':'form-control'}),
            'pages': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'retal_price_day': forms.NumberInput(attrs={'class':'form-control', 'id':'retalpriceday'}),
            'retal_period': forms.NumberInput(attrs={'class':'form-control', 'id':'retalperiod'}),
            'total_rental': forms.NumberInput(attrs={'class':'form-control', 'id':'totalrental'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }


class PathForm(forms.Form):
    start_city = forms.ModelChoiceField(queryset=City.objects.all(), label="اختر مكان البداية")
    end_city = forms.ModelChoiceField(queryset=City.objects.all(), label="اختر مكان النهاية")


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']


class RoadForm(forms.Form):
    city1 = forms.ModelChoiceField(queryset=City.objects.all(), label="اختر المدينة الأساسية")
    city2 = forms.ModelChoiceField(queryset=City.objects.all(), label="اختر المدينة المجاورة")
    distance = forms.FloatField(label="المسافة")




