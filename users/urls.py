from django.urls import path

from users.views import log,reg

app_name = 'users' # для чего ее указывать? чтобы в urls можно так ссылаться products:index

urlpatterns = [
    path('login/', log, name='login'),
    path('registration/', reg, name='registration')
]