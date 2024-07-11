/* Definición y tipo de variables
Una varaible es un contenedor de información. El contenido de las variables pueden cambiar durante la ejecución del programa.
Vamos a trabajar en lowerCamelCase (Primera palabra en minúsculas, el resto de palabras comienzan con mayúscula)
No se permiten símbolos como $, %, @, +, -, etc para las variables.
Tampoco debemos poner una letra mayúscula al comienzo de una variable, porque las clases son las que empiezan con mayúsculas.
*/

//package variables;
// Este el paquete principal del proyecto

/*
 * @author Carlos
 */
public class Variables_p4_t1{
    public static void main(String[] args) {
        //Aquí establecemos nuestro código.
        //Enteros (int y long)

        int x; //Declaración de variable
        x = 7; //Asignación de valor
        System.out.println(x);
        x= x * 8;
        System.out.println(x);

        //Si queremos almacenar valores muy grandes
        //usaremos long en luger de int

        //Números decimales (double y float)

        double y, z; //Declaramos dos (o más) variables a la vez.
        // double y; (Estándar de Google)
        // double z; 
        y= 9;   //Asignación de valor a las variables
        z = 24.02; 
        System.out.println(x+y);

        // Cadenas de caracteres (String)
        String starPlatinum = "Ora Ora Ora";
        String ataqueFinal = "Star finger!";
        // Definir y asignar valor a la variable
        System.out.println("Ataca! " + starPlatinum + " ...Bien!, ahora usa... " + ataqueFinal);

        //Una cadena de caracteres ouede ser una cadena vacía
        String cadenaVacia = "";

    }
}
