package Quiz;

import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.CardLayout;
import java.util.Random;
import javax.swing.JOptionPane;

public class Quiz extends JFrame{
	JPanel p=new JPanel();
	CardLayout cards=new CardLayout();
	int numQs;
	int wrongs=0;
	int total=0;
	
	String[][] answers={
		{"Enschede","Amsterdam","Den Haag","Berlin"},
		{"Slang for Hankechief","Dutch for Keyboard","A Male Sheep","Width of a Cut"},
		{"Euler","Erasmus","Fibonnaci","Archemides"},
		{"Shadow of the Collosus","Lighthouse of Alexandria","Colliseum","Parthanon"},
		{"Cars","Nothing","Planes","Plastic Materials"},
		{"True","False"},
		{"True","False"},
		{"4","5","6","7"},
		{"The Lion King","Hamlet","Death of The Salesmen","Phantom of the Opera"},
	};
	
	RadioQuestions questions[]={
		
		new RadioQuestions(
			"What is the capital of the Netherlands?",
			answers[0],
			1,this
		),
		new RadioQuestions(
			"What is a kerf?",
			answers[1],
			3,this
		),
		new RadioQuestions(
			"Who discovered the number e?",
			answers[2],
			0,this
		),
		new RadioQuestions(
			"Which of the following is one of the 7 wonders of the ancient world?",
			answers[3],
			1,this
		),
		new RadioQuestions(
			"Which of the following is not made in China?",
			answers[4],
			1,this
		),
		new RadioQuestions(
			"True or False, Driving drunk is more dangerous than driving tired",
			answers[5],
			1,this
		),
		new RadioQuestions(
			"True or False, The Platypus is a mammal",
			answers[6],
			0,this
		),
		new RadioQuestions(
			"How many strings are there on a standard guitar?",
			answers[7],
			2,this
		),
		new RadioQuestions(
			"Which of these plays is made by shakespeare?",
			answers[8],
			1,this
		)
	};

	public static void main(String args[]){
		new Quiz();
	}
	
	public Quiz(){
		super("Quiz Game");
		setResizable(true);
		setSize(500,400);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		p.setLayout(cards);
		numQs=questions.length;
		for(int i=0;i<numQs;i++){
			p.add(questions[i],"q"+i);
		}
		Random r=new Random();
		int i=r.nextInt(numQs);
		cards.show(p,"q"+i);
		add(p);
		setVisible(true);
	}
	
	public void next(){
		if((total-wrongs)==numQs){
			showSummary();
		}else{
			Random r=new Random();
			boolean found=false;
			int i=0;
			while(!found){
				i=r.nextInt(numQs);
				if(!questions[i].used){
					found=true;
				}
			}
			cards.show(p,"q"+i);
		}
	}
	
	public void showSummary(){
		JOptionPane.showMessageDialog(null,"All Done :), here are your results"+
			"\nNumber of incorrect Answers: \t"+wrongs+
			"\nNumber of Correct Answers: \t"+(total-wrongs)+
			"\nAverage Incorrect Answers per Quesiotn: \t"+((float)wrongs/numQs)+
			"\nPercent Correct: \t\t"+(int)(((float)(total-wrongs)/total)*100)+"%"
		);
		System.exit(0);
	}
}
