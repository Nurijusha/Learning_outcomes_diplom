from django.urls import path, include

from .views import ActivateUser

app_name = 'users'

urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('activate-account/<str:uid>/<str:token>', ActivateUser.as_view()),
]