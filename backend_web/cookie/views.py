from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from cookies.models import Cookie
from rest_framework import viewsets
from .serializers import CookieSerializer


class CookieViewSet(viewsets.GenericViewSet):
    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer

    @action(methods=["POST"], detail=False, permission_classes=[AllowAny])
    def add_cookie(self, request):
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



