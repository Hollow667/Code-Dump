import java.net.MalformedURLException;
import java.net.URL;
 
public class MyRelativeUrl {
 
    public static void main(String a[]){
        try {
            URL main = new URL("http://www.java2novice.com");
            URL relative = new URL(main,"/java_thread_examples/");
            System.out.println(relative.toString());
        } catch (MalformedURLException ex) {
 
        }
    }
}

