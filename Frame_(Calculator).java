import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JOptionPane;

public class Frame1 {

	private JFrame frame;
	private JTextField num1;
	private JLabel lblMessage;
	private JTextField num2;
	private JButton btnNewButton_1;
	private JTextField answer;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Frame1 window = new Frame1();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public Frame1() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		JButton btnNewButton = new JButton("Add");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				int number1,number2,ans;
				try {
					number1 = Integer.parseInt(num1.getText());
					number2 = Integer.parseInt(num2.getText());
					
					ans = number1 + number2;
					answer.setText(Integer.toString(ans));
					
				}catch(Exception e1){
						
						JOptionPane.showMessageDialog(null, "Please enter valid numbers");
			}
				
			}
		});
		btnNewButton.setBounds(101, 188, 89, 23);
		frame.getContentPane().add(btnNewButton);
		
		num1 = new JTextField();
		num1.setBounds(101, 54, 264, 20);
		frame.getContentPane().add(num1);
		num1.setColumns(10);
		
		lblMessage = new JLabel("The anwer is:");
		lblMessage.setBounds(151, 116, 158, 54);
		frame.getContentPane().add(lblMessage);
		
		num2 = new JTextField();
		num2.setBounds(101, 85, 264, 20);
		frame.getContentPane().add(num2);
		num2.setColumns(10);
		
		btnNewButton_1 = new JButton("Subtract");
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				int number1,number2,ans;
				try {
					number1 = Integer.parseInt(num1.getText());
					number2 = Integer.parseInt(num2.getText());
					
					ans = number1 - number2;
					answer.setText(Integer.toString(ans));
					
				}catch(Exception e2){
						
						JOptionPane.showMessageDialog(null, "Please enter valid numbers");
			}
				
			}
		});
		btnNewButton_1.setBounds(276, 188, 89, 23);
		frame.getContentPane().add(btnNewButton_1);

		
		answer = new JTextField();
		answer.setBounds(233, 133, 86, 20);
		frame.getContentPane().add(answer);
		answer.setColumns(10);
	}
}
