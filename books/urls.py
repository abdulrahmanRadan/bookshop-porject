from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index, name='index'),
    path('book',views.show, name='books'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('deletecat/<int:id>', views.deletecat, name='deletecat'),
    path('graph/', views.graph_view, name='graph_view'),
    path('add_city/', views.add_city, name='add_city'),
    path('add_road/', views.add_road, name='add_road'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]
