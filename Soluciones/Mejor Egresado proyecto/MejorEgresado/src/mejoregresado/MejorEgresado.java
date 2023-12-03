package mejoregresado;

import java.util.Scanner;

public class MejorEgresado {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int numEstudiantes, cont;
        double promedio, promMayor = 0;
        String nombres = null, nombre;//Iniciaializamos las variables string en null que es el equivalente de 0 en string
        System.out.println("Cuantos estudiantes desea ingresar:");//Ingrese la cantidad de estudiantes
        numEstudiantes = teclado.nextInt();
        for (cont = 0; cont < numEstudiantes; cont++) {//Se utiliza ciclo repetitivo for
            System.out.println("Ingrese el nombre del estudiante: ");
            nombre = teclado.next();
            System.out.println("Ingrese el promedio final del estudiante: ");
            promedio = teclado.nextDouble();
            if (promedio == promMayor) {
                nombres += " y " + nombre; // Si hay más de un estudiante con el promedio más alto
            } else if (promedio > promMayor) {
                promMayor = promedio; // Se asigna el mayor promedio
                nombres = nombre;
            }
        }
        System.out.println("--------------------------------------------------------------------------------------------------");
        System.out.println("FRUTO DE SU GRAN ESFUERZO Y DEDICACION SE LE OTORGA UN RECONOCIMIENTO A: " + nombres + ". POR HABER CONSEGUIDO EL PROMEDIO MAS ALTO, SIENDO ESTE DE: " + promMayor);
    }
}
/*Cuantos estudiantes desea ingresar:
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
BUILD SUCCESSFUL (total time: 35 seconds)
*/