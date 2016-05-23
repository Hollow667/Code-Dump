
public class Recursion {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(fact(5));
		
		//5 factorial = 120

	}
	
	//fact
	public static long fact(long n){
		if(n <= 1)
			return 1;
		else
			return n * fact(n-1);
		
	}

}
