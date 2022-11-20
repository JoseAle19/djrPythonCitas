from .models import UsersModel, PatientAppointmentModel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializaers import LoginUserSerializer, RegisterUserSerializer, AppointmentSerializer, FinishAppointmentSerializer, UserSerializer
from .validates import validateHour
import re



def isValidEmail(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None

@api_view(['POST'])
def user_login(request):
    if request.method =='POST':
        infoUser = request.data
        
        # Validar si el cliente no manda correo
        if infoUser['email'] == '':
             return Response({
              'Status': False,
              'Message':'Correo vacio'
          })
        
        
        # Validar si existe el correo del usuario a iniciar sesion
        emailUser = UsersModel.objects.filter(email= infoUser['email'])
        email_user_serializer = LoginUserSerializer(emailUser, many = True)

        if len(email_user_serializer.data)<1:
            return Response({
                'Status': False,
                'Message':'Correo no existe'
            })
            
# Validar si el cliente no manda contrasenia del correo
        if infoUser['password'] == '':
          return Response({
              'Status': False,
              'Message':'Contraseña vacia'
          })
        
        passwordUser = UsersModel.objects.filter(password= infoUser['password'])
        password_user_serializer = LoginUserSerializer(passwordUser, many = True)
        if len(password_user_serializer.data)<1:
          return Response({
              'Status': False,
              'Message': 'Contraseña incorrecta'
          })
        #Obtener los todos los datos del usuario
        dataUser  = UsersModel.objects.all().filter(email = infoUser['email'])
        dataUserSerializer = LoginUserSerializer(dataUser, many= True)
        data=dataUserSerializer.data
        user={
            'email': data[0]['email'],
            'rol': data[0]['rol']
             
        }
        return Response({
                'Status': True,
                'Message':'Hola, bienvenido '+ str(infoUser['email']),
                'Data': user
            })
    

@api_view(['POST'])
def user_register(request):    
    if request.method == 'POST':
        user = request.data
        user_serializer  = RegisterUserSerializer(data = user)
        if user_serializer.is_valid():
            # Validar corrreo 
            if isValidEmail(user['email']) == False:
                return Response({
                 'Status': False,
                'Message':'Correo no valido',
                })
            user_serializer.save()
            return Response({
                'Status': True,
                'Message':'Registro exitoso',
                'Data': user_serializer.data
            }, status= status.HTTP_201_CREATED )
        else:
               return Response({
                'Status': False,
                'Message':'Erro al registrarse',
                'Data': user_serializer.errors
            }, status= status.HTTP_400_BAD_REQUEST)

    

@api_view(['POST'])
def create_appointment(request):
    appointment = AppointmentSerializer(data= request.data)
    appointments = PatientAppointmentModel.objects.all()
    appointmentsSerializer = AppointmentSerializer(appointments, many= True)
    # Validar si ya hay 4 citas en este dia 
    
    appointmentDate = AppointmentSerializer( PatientAppointmentModel.objects.all().filter(dateAppointment = request.data['dateAppointment']), many = True)

    if len(appointmentDate.data) >= 4:
       return Response({
                'Status': False,
                'Message':'No hay disponibilidad en este dia',
            })
    
    if appointment.is_valid():    
        return validateHour(appointmentsSerializer.data, request.data, appointment)
    
    return Response({
            "Status": False,
            "Errors": appointment.errors
        })
        
        
        
        
# 
@api_view(['GET'])
def list_appointment(request, finish):
    appointment = AppointmentSerializer(PatientAppointmentModel.objects.all().filter(statustAppointment = True), many= True)
    if finish == 1:
        appointment = AppointmentSerializer(PatientAppointmentModel.objects.all().filter(statustAppointment = False), many= True)
        return Response({
            'Status': True,
            'Counts': len(appointment.data),
            'Message': 'Citas pendientes',
            'appointmentsNoFinish': appointment.data
        }, status= status.HTTP_200_OK)
    return Response({
        'Status': False,
        'Message': 'No hay citas, por ahora',
        'Counts': len(appointment.data),
        'appointmentsFinish': appointment.data
    })
        
        





@api_view(['PUT'])     
def finishAppointment(request, id):
    appointment = PatientAppointmentModel.objects.filter(id = id).first()
    dataAppo =  FinishAppointmentSerializer(appointment, data= request.data)
    if appointment is None:
        return Response(
            {
            'Status': False,
            'Message':'No existe una cita con este id'
            }, status= status.HTTP_400_BAD_REQUEST)
    if dataAppo.is_valid():
       dataAppo.save()
       return Response({
                  'Status':True,
                  'Message': 'Cita finalizada',
                  'data': dataAppo.data
                      })

    return Response({
        'Status': False,
        'Message': 'Error al terminar la cita',
        'Data': dataAppo.errors
    })
    
    
@api_view(['GET'])
def listUsers(request):
    users = UsersModel.objects.all()
    usersSerializer = UserSerializer(users, many = True)
    if len(usersSerializer.data) < 1:
           return Response({
        'Status': False,
        'Message': 'No hay ningun usuario en la base de datos',
        'Counts': len(usersSerializer.data),
        'Users': usersSerializer.data,
            })
    return Response({
        'Status': True,
        'Message': 'Usuarios en la base de datos',
        'Counts': len(usersSerializer.data),
        'Users': usersSerializer.data,
    })