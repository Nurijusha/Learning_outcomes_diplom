import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions


class ActivateUser(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, uid, token):
        """ Activation url after register new user. """
        payload = {'uid': uid, 'token': token}

        url = "http://localhost:8000/users/activation/"
        response = requests.post(url, data=payload)

        if response.status_code == 204:
            return Response({'Поздравляем'}, response.status_code)
        else:
            return Response(response.json())
        # TODO: добавить шаблон подтверждения регистрации
        # TODO: добавить шаблон подтверждения активации
