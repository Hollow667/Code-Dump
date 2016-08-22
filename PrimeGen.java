import java.util.Scanner;

public class primeGen {
    public static void main(String[] arrstring) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("\n(max 999999999)");
        System.out.println("\nGenerare pana la :");
        int n = scanner.nextInt();
        Scanner scanner2 = new Scanner(System.in);
        System.out.println("\nGenerare de la :");
        for (int i = scanner2.nextInt(); i < n; ++i) {
            boolean bl = true;
            for (int j = 2; j < i; ++j) {
                if (i % j != 0) continue;
                bl = false;
                break;
            }
            if (!bl) continue;
            System.out.print("" + i + " ");
        }
    }
}
