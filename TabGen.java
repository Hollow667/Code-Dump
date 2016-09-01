import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.Date;
import java.text.DateFormat;
import java.text.SimpleDateFormat;

public class TabGen {

    public static void tabGen(String f, String t, int n, int l) {
        
        DateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        Date date = new Date();
	    StringBuffer partBuffer = new StringBuffer();

        try {
            File file = new File(f + ".txt");
            if (file.exists()) {
                file.createNewFile();
            }
            PrintWriter pw = new PrintWriter(file);
            pw.println("\n");
            pw.println("    " + t);
            pw.println("    " + dateFormat.format(date));

	        for(int k = l; k > 0; k--) {
		    partBuffer.append("-");
	        }
		    String var = partBuffer.toString();

            for(int i = n; i > 0; i--) {
                pw.println("\n");
		        pw.println(var);
		        pw.println(var);
		        pw.println(var);
		        pw.println(var);
		        pw.println(var);
		        pw.println(var);
            }
            pw.close();           

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {

        Scanner one = new Scanner(System.in);
        System.out.println("\nDenumirea fisierului :");
        String file = one.next();

        Scanner two = new Scanner(System.in);
        System.out.println("\nTitlul tabulaturii :");
        String title = two.next(); 

        Scanner three = new Scanner(System.in);
        System.out.println("\nNumarul de linii :");
        int lines = three.nextInt();

        Scanner four = new Scanner(System.in);
        System.out.println("\nLungimea liniilor :");
        int length = four.nextInt();
        
        tabGen(file,title,lines,length);
        System.out.println("\nDone.");
    }
}

