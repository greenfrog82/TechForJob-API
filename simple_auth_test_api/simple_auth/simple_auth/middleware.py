from django.conf import settings
from django.http import JsonResponse

class SimpleAPIAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        api_key = request.POST.get('api_key') or request.GET.get('api_key') or request.META.get('HTTP_X_APIKEY')
        if not api_key or api_key != settings.API_KEY:
            return JsonResponse({'error': 'bad api key'}, status=400)
