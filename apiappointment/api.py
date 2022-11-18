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
    
    
    
@api_view(['POST'])
def appointmentUser(request, flag):
    userEmail = request.data



    appointUser = AppointmentSerializer(
      PatientAppointmentModel.objects.filter(emailPatient = userEmail['email'], statustAppointment = True) , many=True)

    if flag == 0:
      appointUser = AppointmentSerializer(
      PatientAppointmentModel.objects.filter(emailPatient = userEmail['email'], statustAppointment = False) , many=True)
      return Response({
        'Status': True,
        'Message': 'Citas terminadas',
        'Counts': len(appointUser.data),
        'Appointment': appointUser.data

      })
      
    return Response({
      'Status': True,
      'Message': 'Citas Pendientes',
      'Counts': len(appointUser.data),
      'Appointment': appointUser.data
    })



@api_view(['DELETE'])
def deleteAppointment(request, id):
  appointmetDelete = AppointmentSerializer(
    PatientAppointmentModel.objects.filter(id = id).first(),)
  
  if appointmetDelete.data['namePatient'] == '':
      return Response({
        'Status': False,
        'Message':'No hay ninguna cita con el id '+ str(id)
      })
  PatientAppointmentModel.objects.filter(id = id).first().delete()
  return Response({
    'Status': True,
    'Message':'Cita eliminada con el id '+ str(id),
  })
  