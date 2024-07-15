import java.util.Scanner; // Para entrada de datos desde teclado

/**
 * Clase DatosDesdeTeclado para demostrar la entrada de datos desde teclado y su procesamiento.
 * 
 * @author Carlos
 */
public class DatosDesdeTeclado {

    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        String nombre;
        System.out.println("Dime como te llamas");
        nombre = s.nextLine();
    
        System.out.println("Tu nombre es: " + nombre);

        String primerNum;
        System.out.print("Introduce un número entero: ");
        primerNum = s.nextLine();
        // Declaro e inicializo la variable
        System.out.println("Has introducido el " + primerNum);

        // Ahora trabajaremos con decimales
        double x1, x2, x3;
        System.out.println("Introduce tres números decimales");
        x1 = s.nextDouble();
        x2 = s.nextDouble();
        x3 = s.nextDouble();
        double media = (x1 + x2 + x3) / 3;
        System.out.println("La media de los tres números es: " + media);

        s.close();
    }
}
