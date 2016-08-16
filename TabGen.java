import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.Date;
import java.text.DateFormat;
import java.text.SimpleDateFormat;

public class TabGen {

    public static void tabGen(int n, String t) {
        
        DateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        Date date = new Date();
        try {
            File file = new File("newFile.txt");
            if (file.exists()) {
                file.createNewFile();
            }
            PrintWriter pw = new PrintWriter(file);
            pw.println("\n");
            pw.println("    " + t);
            pw.println("    " + dateFormat.format(date));
            for(int i = n; i > 0; i--) {
                pw.println("\n");
                pw.println("----------------------------------------------------------------------");
                pw.println("----------------------------------------------------------------------");
                pw.println("----------------------------------------------------------------------");
                pw.println("----------------------------------------------------------------------");
                pw.println("----------------------------------------------------------------------");
                pw.println("----------------------------------------------------------------------");

            }
            pw.close();           

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {

        Scanner one = new Scanner(System.in);
        System.out.println("\nTitlul tabulaturii :");
        String title = one.next(); 

        Scanner two = new Scanner(System.in);
        System.out.println("\nNumarul de linii :");
        String response = two.next();
        Integer lines = Integer.valueOf(response);
        
        tabGen(lines,title);
        System.out.println("\nDone.");
    }
}




