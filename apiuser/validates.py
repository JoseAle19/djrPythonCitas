from rest_framework.response import Response


def validateHour(data, dataUser, appointment):
     print(dataUser)
     for item in data:
            if item['appointmentTime'] == dataUser['appointmentTime'] :                   
                return Response({
                    'Status': False,
                    'Message': 'Ya hay una cita a esta hora'    
                })
     appointment.save()
     return Response({
            "Status":True,
            "Data":appointment.data
        })