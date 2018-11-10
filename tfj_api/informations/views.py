from django.http import JsonResponse

def perform(request):
    return JsonResponse({'result': 'success'})
