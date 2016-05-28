import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTextArea;


public class MainFrame extends JFrame {
	
	private DetailsPanel detailsPanel;
	
	public MainFrame(String title){
		super(title);
		
		// set layout manager
		setLayout(new BorderLayout());
		
		
		// create swing component
		final JTextArea textArea = new JTextArea();
		//JButton button = new JButton("Click me!");
		
		detailsPanel = new DetailsPanel();
		
		detailsPanel.addDetailListener(new DetailListener(){
			public void detailEventOccured(DetailEvent event){
				String text = event.getText();
				
				textArea.append(text);
			}
		});
		
		// add swing component to content pane
		Container c = getContentPane();
		
		c.add(textArea, BorderLayout.CENTER);
		//c.add(button, BorderLayout.SOUTH);
		c.add(detailsPanel, BorderLayout.WEST);
		
		// add behaviour
		//button.addActionListener(new ActionListener() {

			//@Override
			//public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				//textArea.append("Hello\n");
				
			//}
			
		//});
		
	}	

}
