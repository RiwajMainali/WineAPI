from django.http import JsonResponse
import json
def api_home(request, *args, **kwargs):
    body= request.body

    data = json.loads(body)
    return JsonResponse(data)

# Create your views here.
