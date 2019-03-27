from django.http import JsonResponse

from cookies.models import Cookie
from rest_framework import viewsets
from .serializers import CookieSerializer


class CookieViewSet(viewsets.GenericViewSet):
    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer

    @staticmethod
    def create(request):
        data = request.data

        name = data['name']
        archive = data['archive']

        cookie = Cookie.objects.create(
            name=name,
            archive=archive
        )

        print(cookie)

        if cookie:
            return JsonResponse({
                'success': True,
                'message': 'Salvo',
                'status': 200,
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Rejeitado',
                'status': 200,
            })



