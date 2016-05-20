package Exercises;

public class ExerciseB {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] nums = {"10", "20", "30", "40"};
		
		int total = 0;
		
		for(String temp : nums){
			total += Integer.parseInt(temp);
		}
		
		System.out.println("Total = " + total);
	}

}
