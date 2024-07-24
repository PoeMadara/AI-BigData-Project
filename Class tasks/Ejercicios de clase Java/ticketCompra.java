// Tarea: Hacer un ticket de compra

// package ticketCompra

/*
 * Author Carlos
 */

 public class ticketCompra {
    public static void main(String [] args) {

        System.out.println("Artículo        Precio/Caja    NºCajas");
        System.out.println("---------------------------------------");
        System.out.printf("%-14s   %8.2f    %6d\n", "\u001B[32mManzanas", 3.5, 10);
        System.out.printf("%-14s   %8.2f    %6d\n", "\u001B[31mFresas", 6.25, 20);
        System.out.printf("%-14s   %8.2f    %6d\n", "\u001B[33mPlátanos", 2.75, 15);
        System.out.printf("%-20s   %8.2f    %6d\n", "\u001B[38;5;214mNaranjas", 4.0, 12);
        System.out.printf("%-14s   %8.2f    %6d\n", "\u001B[35mUvas", 5.5, 18);
        System.out.printf("%-14s   %8.2f    %6d\n", "\u001B[36mPeras", 3.0, 25);

        // Reset color
        System.out.print("\u001B[0m");
    }
}
