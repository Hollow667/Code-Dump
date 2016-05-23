import javax.swing.JFrame;
public class ClientTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		IM_Client charlie;
		charlie = new IM_Client("127.0.0.1");
		charlie.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		charlie.startRunning();
	}

}
