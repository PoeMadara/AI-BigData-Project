/*La sentencia if permite la ejecución de una serie de instrucciones en función
del resultando en una expresión lógica. El resultado será siempre verdadero o 
falso (Valores booleanos). "Si esta condición se cumple haz esto, sino haz lo 
otro"

if (condición) {
    instrucciones a ejecutar si la condición es verdadera
}else{
    instrucciones a ejecutar una condición si es falsa
}
*/
//package condicional;

import java.util.Scanner; // Importación de la clase Scanner

/**
 *
 * @author Carlos
 */
public class Condicional {
    public static void main(String[] args) { // El método main es el punto de entrada de la aplicación
        // Vamos a trabajar con ejemplos simples
        Scanner sc = new Scanner(System.in, "ISO-8859-1"); // Definimos nuestro scanner

        /* 
        String miFruta = "manzana";
        if ("naranja".equals(miFruta)){ // Si naranja es igual a manzana
            System.out.println("Las frutas son iguales");
        } else { // Si no
            System.out.println("Las frutas no son iguales");
        }
        */

        /*
        System.out.println("Cuál es la capital de Brasil"); // Pregunta al usuario
        String respuesta = sc.nextLine(); // Lee la respuesta del usuario

        if (respuesta.equals("Brasilia")) { // Verifica si la respuesta es correcta
            System.out.println("La respuesta es correcta"); // Respuesta correcta
        } else {
            System.out.println("La respuesta no es correcta"); // Respuesta incorrecta
        }
        */

        /*
        System.out.print("Introduce por favor un número entero: ");
        int x = sc.nextInt();

        if (x < 0) {
            System.out.println("El número introducido es negativo");
        } else if (x > 0) {
            System.out.println("El número introducido es positivo");
        } else {
            System.out.println("El número introducido es 0");
        }
        */

        /*
         * TABLA DE OPERADORES DE COMPARACIÓN:
         * == igual (Ejemplo a==b)
         * != distinto (a!=b)
         * < menor que
         * > mayor que
         * <= menor o igual que
         * >= mayor o igual que
         */

        /* TABLA DE OPERADORES LÓGICOS
         * && -----> y -----> (a > b) && (b < c) ---> Las dos condiciones deben de ser verdaderas.
         * || -----> o -----> (a > b) || (b < c) ---> Al menos una de las dos condiciones deben de ser verdaderas
         * !  -----> no -----> !(a > b) ---> Verdadero si la condición es falsa
         */

        /*
        // TABLA DE LA VERDAD
        boolean a = true;
        boolean b = false;
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        System.out.println("&& = " + (a && b));
        System.out.println("|| = " + (a || b));
        System.out.println("!a = " + !a);
        System.out.println("a || (9 > 10) = " + (a || (9 > 10)));
        System.out.println("((5 <= 5) || false) && (!a) = " + (((5 <= 5) || false) && (!a)));
        */

        // SISTEMA DE SELECCIÓN MÚLTIPLE
        System.out.println("Introduce un día de la semana (en número): ");
        int diaSemana = sc.nextInt();

        String nombreDia;

        switch (diaSemana) {
            case 1:
                nombreDia = "lunes";
                break;
            case 2:
                nombreDia = "martes";
                break;
            case 3:
                nombreDia = "miércoles";
                break;
            case 4:
                nombreDia = "jueves";
                break;
            case 5:
                nombreDia = "viernes";
                break;
            case 6:
                nombreDia = "sábado";
                break;
            case 7:
                nombreDia = "domingo";
                break;
            default:
                nombreDia = "no es un día de la semana";
                break;
        }

        System.out.println("El día " + diaSemana + " es " + nombreDia);

        String comidaDia = ""; // Declarar fuera del bloque if para que sea accesible más tarde

        if (diaSemana >= 1 && diaSemana <= 7) {
            switch (diaSemana) {
                case 1:
                    comidaDia = "Pollo con patatas";
                    break;
                case 2:
                    comidaDia = "Pescado con verduras";
                    break;
                case 3:
                    comidaDia = "Sopa de garbanzos";
                    break;
                case 4:
                    comidaDia = "Cerdo a la plancha y verduras";
                    break;
                case 5:
                    comidaDia = "Curry con arroz";
                    break;
                case 6:
                    comidaDia = "Pescado con patatas";
                    break;
                case 7:
                    comidaDia = "Pizza";
                    break;
            }
            System.out.println("Hoy " + diaSemana + " y te toca comer " + comidaDia);
        } else {
            System.out.println("No es un día de la semana válido.");
        }

        sc.close();
    }
}
