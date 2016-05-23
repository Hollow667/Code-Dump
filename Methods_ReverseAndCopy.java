import java.util.*;
public class Methods_ReverseAndCopy {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//create an array and convert to list
		Character[] ray = {'p', 'w', 'n'};
		List<Character> l = Arrays.asList(ray);
		System.out.println("List is : ");
		output(l);
		
		//reverse and print out the list
		Collections.reverse(l);
		System.out.println("After reverse : ");
		output(l);
		
		//create new array and new list
		Character[] newRay = new Character[3];
		List<Character> listCopy = Arrays.asList(newRay);
		
		//copy contents of list into listcopy
		Collections.copy(listCopy, l);
		System.out.println("Copy of list : ");
		output(listCopy);
		
		//fill collection with crap
		Collections.fill(l, 'X');
		System.out.println("After filling the list : ");
		output(l);
	}
	
	//output method
	private static void output(List<Character> theList){
		for(Character thing: theList)
			System.out.printf("%s ", thing);
		
		System.out.println();
	}
}
