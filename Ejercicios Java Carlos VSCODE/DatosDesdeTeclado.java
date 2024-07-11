/*Entrada desde teclado o desde cualquier otro dispositivo
Procesamiento en los datos para producir los resultados
Visualización por pantalla
 */

//package datosdesdeteclado
import java.util.Scanner; //Para entrada de datos desde teclado
/*
 * @author Carlos
 */

public class DatosDesdeTeclado{

    public static void main(String[] args) {
        
        Scanner s = new Scanner (System.in);
        String nombre;
        System.out.println("Dime como te llamas");
        nombre = s.nextLine();
    
        System.out.println("Tu nombre es: " + nombre);

        String primerNum;
        System.out.print("Introduce un número entero: ");
        primerNum = s.nextLine();
        //Declaro e inicializo la variable
        System.out.println("Has introducido el " + primerNum);

        //Ahora trabajaremos con decimales
        /* 
        double x1, x2, x3;
        System.out.println("Introduce un número");
        x1 = s.nextDouble();
        System.out.println("Introduce el siguiente");
        x2 = s.nextDouble();
        System.out.println("Introduce el siguiente");
        x3 = s.nextDouble();
        suma = x1 + x2 + x3;
        double media = suma/3;

        System.out.println("La media es: " + media);
        */

        double x1, x2, x3;
        System.out.prinln("Introduce tres números decimales");
        x1 = s.nextDouble();
        x2 = s.nextDouble();
        x3 = s.nextDouble();
        double media = (x1 + x2 + x3) / 3;
        System.out.prinln(" La media de los tres números es: " + media);

        s.close();
        }
    }