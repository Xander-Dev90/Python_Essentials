
def calcular_tiempo(hora_inicio, min_inicio, duracion):
    # Convertir las horas de inicio y fin a minutos
    hora_inicio= (hora_inicio +(min_inicio+ duracion)//60)%24
    minutos_fin = (min_inicio + duracion)%60
    print("La hora de finalizacion es: ", hora_inicio,":",minutos_fin)

hora_inicio = int(input("Ingrese la hora de inicio (0-23): "))
min_inicio = int(input("Ingrese los minutos de inicio (0-59): "))
duracion = int(input("Ingrese la duración en minutos: "))

calcular_tiempo(hora_inicio, min_inicio, duracion)