# Descripción: Ejercicios de Programación Orientada a Objetos
def ejercicio_hora():
   
    hour = int(input("Hora de inicio (horas): "))
    mins = int(input("Minuto de inicio (minutos): "))
    dura = int(input("Duración del evento (minutos): "))

    mins += dura
    # sumar las horas y los minutos si los minutos son mayores a 60
    hour += mins // 60
    mins %= 60
    # calcular la hora en formato de 24 horas
    hour %= 24
    print("Hora de finalización:", hour)
    print("Minuto de finalización:", mins)

    print("Hora de finalización: %d:%02d" % (hour, mins))

ejercicio_hora()
# ##########################################################################################

# Descripción: Crear una clase llamada Person y crear un objeto llamado myperson

