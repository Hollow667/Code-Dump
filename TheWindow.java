import java.awt.*;
import javax.swing.*;
import javax.swing.event.*;

public class TheWindow extends JFrame {
	
	private JSlider slider;
	private Draw_Oval_withSlide myPanel;

	public TheWindow() {
		super("The title");
		myPanel = new Draw_Oval_withSlide();
		myPanel.setBackground(Color.CYAN);
		
		slider = new JSlider(SwingConstants.HORIZONTAL, 0, 200, 10);
		slider.setMajorTickSpacing(10);
		slider.setPaintTicks(true);
		
		slider.addChangeListener(
				new ChangeListener(){
					public void stateChanged(ChangeEvent e) {
						myPanel.setD(slider.getValue());
					}
				}
		);
		
		add(slider, BorderLayout.SOUTH);
		add(myPanel, BorderLayout.CENTER);

	}
}
