from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('myadmin/', views.admin_login, name='admin'),
    path('myindex/',views.index, name='myindex'),
    path('',views.userindex, name='index'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/',views.profile, name='profile'),

    path('book',views.show, name='books'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('download/<int:book_id>/', views.download, name='download'),
    path('view-pdf/<int:book_id>/', views.view_pdf, name='view_pdf'),




    
    path('deletecat/<int:id>', views.deletecat, name='deletecat'),
    path('graph/', views.graph_view, name='graph_view'),
    path('add_city/', views.add_city, name='add_city'),
    path('add_road/', views.add_road, name='add_road'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]
