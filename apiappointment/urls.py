from rest_framework.urls import path
from .api import listAppointments

urlpatterns =[
path('list_appointment/<int:id>', listAppointments, name='appointments')
]