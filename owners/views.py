import json
from django.views import View
from django.http import JsonResponse
from .models import Owner

# Create your views here.


class OwnerView(View):

    def post(self, request):
        try:
            data = json.loads(request.body)

            Owner.objects.create(
                name=data['name'], age=data['age'], email=data['email'])

            return JsonResponse({'massage': 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'massage': 'INVALID_KEYS'}, status=400)
