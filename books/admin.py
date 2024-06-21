from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Road)
class BooksAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = [  "title", "status", "author"]

admin.site.register(Book, BooksAdmin)