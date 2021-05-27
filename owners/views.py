import json
from django.views import View
from django.http import JsonResponse
from .models import Owner, Dog

# Create your views here.


class OwnerView(View):
    def get(self, request):
        owners = Owner.objects.all()

        result = []
        for owner in owners:
            owner_info = {
                'email': owner.email,
                'name': owner.name,
                'age': owner.age
            }
            result.append(owner_info)

        return JsonResponse({'result': result}, status=200)

    def post(self, request):

        try:
            data = json.loads(request.body)

            Owner.objects.create(
                name=data['name'], age=data['age'], email=data['email'])

            return JsonResponse({'massage': 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'massage': 'INVALID_KEYS'}, status=400)


class DogView(View):
    def get(self, request):
        dogs = Dog.objects.all()

        result = []
        for dog in dogs:
            dog_info = {
                'owner': dog.owner.name,
                'name': dog.name,
                'age': dog.age
            }
            result.append(dog_info)

        return JsonResponse({'result': result}, status=200)

    def post(self, request):
        try:
            data = json.loads(request.body)

            owner = Owner.objects.get(email=data['owner'])
            Dog.objects.create(
                name=data['name'], age=data['age'], owner=owner)

            return JsonResponse({'massage': 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'massage': 'INVALID_KEYS'}, sttus=400)

        except Owner.DoesNotExist:
            return JsonResponse({'massage': 'OWNER DOES NOT EXIST'}, status=400)
