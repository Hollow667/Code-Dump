import java.util.*;
public class Generic_Methods {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Integer[] iray = {1,2,3,4};
		Character[] cray = {'b', 'u', 'c', 'y'};
		
		printMe(iray);
		printMe(cray);
	}
    /*	
	public static void printMe(Integer[] i){
		for(Integer x : i)
			System.out.printf("%s ", x);
		System.out.println();
	}
	
	public static void printMe(Character[] i){
		for(Character x : i)
			System.out.printf("%s ", x);
		System.out.println();
	}*/
	
	// instead of all those overload methods ^
	// we will make a generic method
	public static <T> void printMe(T[] x){
		for(T b : x)
			System.out.printf("%s ", b);
		System.out.println();
	}
}
