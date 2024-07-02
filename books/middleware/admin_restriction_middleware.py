from django.shortcuts import redirect
from django.urls import reverse

class AdminRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/myadmin/') and not request.user.is_superuser:
            return redirect(reverse('home'))
        response = self.get_response(request)
        return response
