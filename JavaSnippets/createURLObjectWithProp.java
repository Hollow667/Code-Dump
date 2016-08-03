import java.net.MalformedURLException;
import java.net.URL;
 
public class MyUrlConstruct {
 
    public static void main(String a[]){
     
        try {
            String protocol = "http";
            String host = "www.java2novice.com";
            int port = 80;
            String path = "/java_thread_examples/";
            URL url = new URL(protocol, host, port, path);
            System.out.println(url.toString());
        } catch (MalformedURLException ex) {
            ex.printStackTrace();
        }
    }
}

