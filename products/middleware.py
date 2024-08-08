from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from person.models import Person

class AdminOnlyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method in ['POST','PUT', 'DELETE']:
            role = request.data.get('role')

            if role != Person.ADMIN:
                return JsonResponse({'error': 'Only admins can perform this action.'}, status=403)

        return None