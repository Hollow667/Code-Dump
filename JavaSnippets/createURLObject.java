import java.net.MalformedURLException;
import java.net.URL;
 
public class MySimpleUrl {
    public static void main(String a[]){
        try {
            String myUrl = "http://www.java2novice.com";
            URL url = new URL(myUrl);
            System.out.println(url.toString());
        } catch (MalformedURLException ex) {
            ex.printStackTrace();
        }
    }
}

