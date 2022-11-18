from rest_framework.urls import path
from .api import listAppointments, appointmentUser, deleteAppointment

urlpatterns =[
path('list_appointment/<int:id>', listAppointments, name='appointments'),
path('appointmentUser/<int:flag>',appointmentUser, name='appointmentUser' ),
path('appointmentDelete/<int:id>',deleteAppointment, name='appointmentDelete' ),
]