num_estudiantes = int(input("Cuantos estudiantes desea ingresar: "))
prom_mayor = 0
nombres = "" #Ingrese la cantidad de estudiantes

for cont in range(num_estudiantes): #Se utiliza ciclo repetitivo for
    nombre = input("Ingrese el nombre del estudiante: ")
    promedio = float(input("Ingrese el promedio final del estudiante: "))
    
    if promedio == prom_mayor:
        nombres += " y " + nombre #Si hay más de un estudiante con el promedio más alto
    elif promedio > prom_mayor:
        prom_mayor = promedio #Se asigna el mayor promedio
        nombres = nombre

print("--------------------------------------------------------------------------------------------------")
print(f"FRUTO DE SU GRAN ESFUERZO Y DEDICACION SE LE OTORGA UN RECONOCIMIENTO A: {nombres}. POR HABER CONSEGUIDO EL PROMEDIO MAS ALTO, SIENDO ESTE DE: {prom_mayor}")
'''
Cuantos estudiantes desea ingresar: 
5
Ingrese el nombre del estudiante: 
Juan
Ingrese el promedio final del estudiante: 
7
Ingrese el nombre del estudiante: 
Carlos
Ingrese el promedio final del estudiante: 
9
Ingrese el nombre del estudiante: 
Jorge
Ingrese el promedio final del estudiante: 
8
Ingrese el nombre del estudiante: 
Daniel
Ingrese el promedio final del estudiante: 
7
Ingrese el nombre del estudiante: 
Pedro
Ingrese el promedio final del estudiante: 
9
--------------------------------------------------------------------------------------------------
FRUTO DE SU GRAN ESFUERZO Y DEDICACION SE LE OTORGA UN RECONOCIMIENTO A: Carlos y Pedro. POR HABER CONSEGUIDO EL PROMEDIO MAS ALTO, SIENDO ESTE DE: 9.0


** Process exited - Return Code: 0 **
Press Enter to exit terminal
'''

