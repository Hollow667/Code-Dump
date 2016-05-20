
public class ExampleString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String x = "Zero Davila";
		
		System.out.println("Hello " + x);
		
		System.out.println(x.toUpperCase());
		
		System.out.println(x.substring(2));
		
		System.out.println(x.substring(2,7));
		
		System.out.println(x.charAt(3));
		
		String age = "37";
		String salary = "78965.83";
		//Wrapper classes
		
		int a = Integer.parseInt(age)/2;
		System.out.println(a);
		
		double s = Double.parseDouble(salary) * .15;
		System.out.println(s);
		
		
		
	}

}
