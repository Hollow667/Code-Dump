import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.lang.Thread;
import java.util.Scanner;

public class Teleprompt {
    public static void main(String[] args) {
	    
        Scanner one = new Scanner(System.in);
        System.out.println("\nDenumirea fisierului :");
        String file = one.next();

        Scanner two = new Scanner(System.in);
        System.out.println("\nMilisecunde intarziere :");
        int seconds = two.nextInt();

        Scanner three = new Scanner(System.in);
        System.out.println("\nSecunde pre :");
        int presec = three.nextInt();

        teleprompter(file,seconds,presec);
        System.out.println("Fuck yeah");
   }

    public static void teleprompter(String f, int s, int p) {
        try (BufferedReader br = new BufferedReader(new FileReader(f))) {
        String line;
        System.out.println();

            for (int i = 1;i<=p;i++) {
                System.out.print("..." + i);
                try {
                    Thread.sleep(1000);
                } catch(InterruptedException e) {
                    System.out.println("We fucked up the sleep thingy");
                }
            }

            System.out.println("\n");
            
            while ((line = br.readLine()) != null) {
                System.out.println(line);
                try {
                    Thread.sleep(s);
                } catch(InterruptedException e) {
                    System.out.println("We fucked up the sleep thingy");
                }
            }
        } catch(IOException e) {
            System.out.println("We fucked up the exception thingy");
        }
    }
}
