from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index, name='index'),
    path('book',views.show, name='books'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('deletecat/<int:id>', views.deletecat, name='deletecat'),
]
