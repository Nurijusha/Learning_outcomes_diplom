import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions


class ActivateUser(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, uid, token):
        """ Activation url after register new user. """
        """protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()"""
        post_url = "http://web:8000/users/activation/"
        post_data = {'uid': uid, 'token': token}
        response = requests.post(post_url, data=post_data)
        if response.status_code == 204:
            return Response({'Поздравляем'}, response.status_code)
        else:
            return Response(response.json())
        # TODO: добавить шаблон подтверждения регистрации
        # TODO: добавить шаблон подтверждения активации
