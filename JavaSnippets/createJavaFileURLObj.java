import java.net.MalformedURLException;
import java.net.URL;
 
public class MyFileUrl {
 
    public static void main(String a[]){
        try {
            URL url = new URL("file://c:/Perl");
            System.out.println(url.toString());
        } catch (MalformedURLException ex) {
            ex.printStackTrace();
        }
         
    }
}

