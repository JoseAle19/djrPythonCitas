from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apiuser.models import PatientAppointmentModel
from apiuser.serializaers import AppointmentSerializer

@api_view(['GET'])
def listAppointments(request, id):
    print(id)
    apppointmentserializer = AppointmentSerializer(PatientAppointmentModel.objects.all().filter(id = id), many = True)

    if len(apppointmentserializer.data) < 1:
      return Response({
      'Message':'No hay ninguna cita con este usuario',
       'Data': apppointmentserializer.data,
       'Counts': len(apppointmentserializer.data)  
      })
    return Response({
      'message':'hola desde controlador de citas xd',
      'Data': apppointmentserializer.data,
      'Counts': len(apppointmentserializer.data)  

    })
    
    
    
# @api_view(['POST'])
# def 

