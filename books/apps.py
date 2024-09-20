from django.apps import AppConfig

from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'your_app_name'

    def ready(self):
        import books.signals  # Import the signals file

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import books.signals

class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'
