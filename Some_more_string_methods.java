
public class Some_more_string_methods {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = "buckyrobertsbuckyroberts";
		
		System.out.println(s.indexOf('k'));
		System.out.println(s.indexOf('k', 5));
		System.out.println(s.indexOf('a'));

		String a = "Bacon ";
		String b = "monster";
		
		System.out.println(a + b);
		System.out.println(a.concat(b));
		System.out.println(a.replace('B', 'F'));
		System.out.println(b.toUpperCase());
		
		String c = "      monster      ";
		
		System.out.println(c.trim());
	}

}
