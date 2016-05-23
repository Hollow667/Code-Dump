import java.util.*;
public class ConvertLists_toArrays {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] stuff = {"babies", "watermelon", "melons", "fudge"};
		java.util.LinkedList<String> thelist = new java.util.LinkedList<String>(Arrays.asList(stuff));
		
		thelist.add("pumpkin");
		thelist.addFirst("firstthing");
		
		// convert back to array
		stuff = thelist.toArray(new String[thelist.size()]);
		
		for(String x : stuff)
			System.out.printf("%s ", x);
		
	}

}
