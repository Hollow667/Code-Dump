import java.io.*;
import java.net.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class IM_Client extends JFrame {
	
	private JTextField userText;
	private JTextArea chatWindow;
	private ObjectOutputStream output;
	private ObjectInputStream input;
	private String message = "";
	private String serverIP;
	private Socket connection;
	
	//constructor
	public IM_Client(String host){
		super("Client mofo!");
		serverIP = host;
		userText = new JTextField();
		userText.setEditable(false);
		userText.addActionListener(
			new ActionListener(){
				public void actionPerformed(ActionEvent event){
					sendMessage(event.getActionCommand());
					userText.setText("");
				}
			}
		);
		add(userText, BorderLayout.NORTH);
		chatWindow = new JTextArea();
		add(new JScrollPane(chatWindow), BorderLayout.CENTER);
		setSize(300,150);
		setVisible(true);
	}
	
	//connect to server
	public void startRunning(){
		try{
			connectToServer();
			setupStreams();
			whileChatting();
		}catch(EOFException eofException){
			showMessages("\n Client terminated connection.");
		}catch(IOException ioException){
			ioException.printStackTrace();
		}finally{
			closeCrap();
		}
	}
	
	//connect to server
	private void connectToServer() throws IOException{
		showMessages("Attempting connection... \n");
		connection = new Socket(InetAddress.getByName(serverIP), 6789);
		showMessages("Connected to:" + connection.getInetAddress().getHostName() );
	}
	
	//set up streams to send and receive messages
	private void setupStreams() throws IOException{
		output = new ObjectOutputStream(connection.getOutputStream());
		output.flush();
		input = new ObjectInputStream(connection.getInputStream());
		showMessages("\n Dude, your streams are now good to go! \n");
	}
	
	//while chatting with server
	private void whileChatting() throws IOException{
		ableToType(true);
		do{
			try{
				message = (String) input.readObject();
				showMessages("\n" + message);
			}catch(ClassNotFoundException classNotfoundException){
				showMessages("\nI dont know that object type.");
			}
			
		}while(!message.equals("SERVER - END"));
	}
	
	//close the streams and sockets
	private void closeCrap(){
		showMessages("\n closing crap down...");
		ableToType(false);
		try{
			output.close();
			input.close();
			connection.close();
		}catch(IOException ioException){
			ioException.printStackTrace();
		}
	}
	
	//send messages to server
	private void sendMessage(String message){
		try{
			output.writeObject("CLIENT - " + message);
			output.flush();
			showMessages("\nCLIENT - " + message);
			
		}catch(IOException ioException){
			chatWindow.append("\n something messed up sending message hoss.");
		}
	}
	
	//change/update chatWindow
	private void showMessages(final String m){
		SwingUtilities.invokeLater(
			new Runnable(){
				public void run(){
					chatWindow.append(m);
				}
			}
		);
	}
	
	//gives user permission to type crap into the text box
	private void ableToType(final boolean tof){
		SwingUtilities.invokeLater(
			new Runnable(){
				public void run(){
					userText.setEditable(tof);
				}
			}
		);
	}
}
