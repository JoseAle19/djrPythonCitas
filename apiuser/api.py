from .models import UsersModel, PatientAppointmentModel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializaers import LoginUserSerializer, RegisterUserSerializer, AppointmentSerializer
from .validates import validateHour
@api_view(['POST'])
def user_login(request):
    if request.method =='POST':
        infoUser = request.data
        # Validar si existe el correo del usuario a iniciar sesion
        emailUser = UsersModel.objects.filter(email= infoUser['email'])
        email_user_serializer = LoginUserSerializer(emailUser, many = True)
        if len(email_user_serializer.data)<1:
            return Response({
                'status': False,
                'message':'Correo no existe'
            })
        
        passwordUser = UsersModel.objects.filter(password= infoUser['password'])
        password_user_serializer = LoginUserSerializer(passwordUser, many = True)
        if len(password_user_serializer.data)<1:
          return Response({
              'status': False,
              'message': 'Contraseña incorrecta'
          })
        #Obtener los todos los datos del usuario
        dataUser  = UsersModel.objects.all().filter(email = infoUser['email'])
        dataUserSerializer = LoginUserSerializer(dataUser, many= True)
        data=dataUserSerializer.data
        user={
            'email': data[0]['email'],
            'rol': data[0]['rol']
             
        }
        print(user)
        return Response({
                'status': True,
                'message':'Hola, bienvenido '+ str(infoUser['email']),
                'data': user
            })
    

@api_view(['POST'])
def user_register(request):    
    if request.method == 'POST':
        user = request.data
        user_serializer  = RegisterUserSerializer(data = user)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'Status': True,
                'Message':'Registro exitoso',
                'data': user_serializer.data
            })
        else:
               return Response({
                'Status': False,
                'Message':'Erro al registrarse',
                'Error': user_serializer.errors
            })

    

@api_view(['POST'])
def create_appointment(request):
    appointment = AppointmentSerializer(data= request.data)
    appointments = PatientAppointmentModel.objects.all()
    appointmentsSerializer = AppointmentSerializer(appointments, many= True)
    if appointment.is_valid():
        
        return validateHour(appointmentsSerializer.data, request.data, appointment)
    else:
        return Response({
            "Status": False,
            "Erros": appointment.errors
        })
        
@api_view(['GET'])
def list_appointment(request, finish):
    appointment = AppointmentSerializer(PatientAppointmentModel.objects.all().filter(statustAppointment = True), many= True)
    if finish == 1:
        appointment = AppointmentSerializer(PatientAppointmentModel.objects.all().filter(statustAppointment = False), many= True)
        return Response({
            'Status': True,
            'Counts': len(appointment.data),
            'appointmentNoFinish': appointment.data
        }, status= status.HTTP_200_OK)
    return Response({
        'Status': True,
        'Counts': len(appointment.data),
        'appointmentFinish': appointment.data
    }, status= status.HTTP_204_NO_CONTENT )
        