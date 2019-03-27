from rest_framework import serializers
from cookies.models import Cookie


class CookieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cookie
        fields = ('name', 'archive')