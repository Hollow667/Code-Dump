
public class Static_Keyword {
//what does the static keyword do in a class?
	public static String DoSomething(String message) {
		//accessed using the class itself
		return message;
		//static members belong to the class instead of
		//a specific instance.
		//a.k.a. shared across all instances.
		
	}
	
	public String DoSomethingElse(String message){
		//accessed using instance of a class
		return message;
	}
}
