
public class Common_String_Methodes {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] words = {"funk", "chunk", "furry", "baconator"};
		
		//startsWith
		for(String w : words){
			if(w.startsWith("fu"))
				System.out.println(w + " starts with fu");
		}
		
		//ends with
		for(String w : words){
			if(w.endsWith("unk"))
				System.out.println(w + " ends with unk");
		}
	}

}
