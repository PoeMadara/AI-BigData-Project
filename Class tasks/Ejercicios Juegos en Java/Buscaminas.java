import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;


//package buscaminas;
/**
 * Juego del Buscaminas en Java. El juego consiste en un tablero donde el jugador debe
 * encontrar un tesoro evitando las minas. El juego se juega en un tablero de 4x4.
 * 
 * El tablero está representado por una matriz de caracteres donde:
 * - 'M' representa una mina.
 * - 'T' representa un tesoro.
 * - '-' representa una celda vacía sin mina ni tesoro.
 * 
 * El jugador tiene 3 intentos para encontrar el tesoro. Puede introducir coordenadas
 * para descubrir el contenido de una celda. El juego indica si hay una mina cerca
 * cuando el jugador selecciona una celda vacía.
 * 
 * @author Carlos
 */
public class Buscaminas {
    private static final int FILAS = 4;
    private static final int COLUMNAS = 4;
    private static final char MINA = 'M';
    private static final char VACIO = '-';
    private static final char TESORO = 'T';

    /**
     * Método principal que inicia el juego.
     */
    public static void main(String[] args) {
        char[][] tablero = new char[FILAS][COLUMNAS];
        initTablero(tablero);
        colocarMinaYTesoro(tablero);
        jugar(tablero);
    }

    /**
     * Inicializa el tablero con celdas vacías.
     * 
     * @param tablero La matriz del tablero de juego.
     */
    private static void initTablero(char[][] tablero) {
        for (int i = 0; i < FILAS; i++) {
            for (int j = 0; j < COLUMNAS; j++) {
                tablero[i][j] = VACIO;
            }
        }
    }

    /**
     * Coloca una mina y un tesoro en posiciones aleatorias en el tablero.
     * 
     * @param tablero La matriz del tablero de juego.
     */
    private static void colocarMinaYTesoro(char[][] tablero) {
        Random aleatorio = new Random();

        // Colocar mina
        int minaX = aleatorio.nextInt(FILAS);
        int minaY = aleatorio.nextInt(COLUMNAS);
        tablero[minaX][minaY] = MINA;

        // Colocar tesoro
        int tesoroX, tesoroY;
        do {
            tesoroX = aleatorio.nextInt(FILAS);
            tesoroY = aleatorio.nextInt(COLUMNAS);
        } while (minaX == tesoroX && minaY == tesoroY); // Asegurarse de que no se coloque la mina y el tesoro en la misma ubicación

        tablero[tesoroX][tesoroY] = TESORO;
    }

    /**
     * Ejecuta el bucle principal del juego, donde el usuario intenta encontrar el tesoro.
     *
     * @param tablero La matriz del tablero de juego.
     */
    private static void jugar(char[][] tablero) {
        Scanner teclado = new Scanner(System.in);
        int intentos = 3;

        System.out.println("Bienvenido al juego de buscaminas. Tienes " + intentos + " intentos.");
        
        while (intentos > 0) {
            int x = -1, y = -1;
            boolean inputValido = false;
            // Verificar que las coordenadas sean correctas
            while (!inputValido) {
                System.out.println("Introduce las coordenadas (fila y columna, Min 0 y Max 3):");
                try {
                    x = teclado.nextInt();
                    y = teclado.nextInt();
                    inputValido = true;
                } catch (InputMismatchException e) {
                    System.out.println("Solo se permiten números válidos. Inténtalo de nuevo.");
                    teclado.next(); // Cerrar el teclado
                }
            }

            if (x < 0 || x >= FILAS || y < 0 || y >= COLUMNAS) {
                System.out.println("Las coordenadas tienen que ser entre 0 y 3. Inténtalo de nuevo.");
                continue;
            }

            if (tablero[x][y] == TESORO) {
                System.out.println("¡Has ganado!");
                teclado.close();
                return;
            } else if (tablero[x][y] == MINA) {
                System.out.println("¡MINA! ¡Has perdido!");
                teclado.close();
                return;
            } else if (hayMinaAlrededor(tablero, x, y)) {
                System.out.println("¡Cuidado! ¡Hay una mina cerca!");
            } else {
                System.out.println("No hay nada aquí.");
            }

            intentos--;
            System.out.println("Te quedan " + intentos + " intentos.");
        }

        System.out.println("Lo siento, has perdido. Gracias por jugar.");
        teclado.close(); // Cerrar el teclado
    }

    /**
     * Verifica si hay una mina en una casilla adyacente a las coordenadas dadas.
     * 
     * @param tablero La matriz del tablero de juego.
     * @param x La coordenada x (fila) a verificar.
     * @param y La coordenada y (columna) a verificar.
     * @return true si hay una mina en una casilla adyacente, false de lo contrario.
     */
    private static boolean hayMinaAlrededor(char[][] tablero, int x, int y) {
        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                if (x + i >= 0 && x + i < FILAS && y + j >= 0 && y + j < COLUMNAS && tablero[x + i][y + j] == MINA) {
                    return true;
                }
            }
        }
        return false;
    }
}
