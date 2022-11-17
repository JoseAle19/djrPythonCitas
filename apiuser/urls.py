from rest_framework.urls import path
from .views import welcome
from .api import user_login, user_register, create_appointment, list_appointment, finishAppointment, listUsers

urlpatterns =[
    path('', welcome, name='welcome'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('create_appointment/',create_appointment , name='create_appointment'),
    path('list_appointment/<int:finish>/',list_appointment, name='list_appointment'),
    path('finish_appointment/<int:id>/', finishAppointment, name='finsh_appointment'),
    path('listUsers/', listUsers, name='listUsers'),
    
]