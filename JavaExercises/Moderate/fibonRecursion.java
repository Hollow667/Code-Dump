public class fibonRecursion {

    static long Fibonacci (int n) {

        return n == 0 ? 0 : (n == 1 ? 1 : (Fibonacci (n - 1) + Fibonacci(n - 2)));
    }

    public static void main (String[] args) {
        for (int f = 0; f < 12; f++) {
            System.out.print(Fibonacci(f) + ", ");
        }
        System.out.println(Fibonacci(12));

    }
}
