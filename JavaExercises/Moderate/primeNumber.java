public Boolean isPrime(Integer n) {
    boolean isPrime = true;
    for (int i = n - 1; i > 1; i--) {
        if (n % i == 0) {
            isPrime = false;
            break;
        }
    }
    return isPrime;
}
