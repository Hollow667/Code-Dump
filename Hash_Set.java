import java.util.*;
public class Hash_Set {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] things = {"apple", "bob", "ham", "bob", "bacon"};
		List<String> list = Arrays.asList(things);
		
		System.out.printf("%s ", list);
		System.out.println();
		
		Set<String> set = new HashSet<String>(list);
		System.out.printf("%s ", set);
	}
}
