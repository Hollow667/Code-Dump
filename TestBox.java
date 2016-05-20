package ClassAndObject;

public class TestBox {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Box ups = new Box();
		Box fedEx = new Box();
		
		ups.length = 5;
		ups.width = 10;
		ups.calculateArea();
		
		fedEx.length = 6;
		fedEx.width = 7;
		fedEx.calculateArea();

	}

}
