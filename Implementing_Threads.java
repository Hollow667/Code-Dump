
public class Implementing_Threads {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Thread t1 = new Thread(new Learning_aboutThreads("one"));
		Thread t2 = new Thread(new Learning_aboutThreads("two"));
		Thread t3 = new Thread(new Learning_aboutThreads("three"));
		Thread t4 = new Thread(new Learning_aboutThreads("four"));
		
		t1.start();
		t2.start();
		t3.start();
		t4.start();
	}
}
