from django.contrib.auth.models import User
from django.http import JsonResponse


def get_list_json(request):
    return JsonResponse({
        'users': list(User.objects.values('id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser'))
    })
