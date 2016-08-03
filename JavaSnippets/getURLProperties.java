import java.net.MalformedURLException;
import java.net.URL;
 
public class MyUrlProperties {
 
    public static void main(String a[]){
     
        try {
            String url =
        "http://www.java2novice.com:80/java_constructor_examples/?query=ok#header";
            URL myUrl = new URL(url);
            System.out.println("Protocol: "+myUrl.getProtocol());
            System.out.println("Host: "+myUrl.getHost());
            System.out.println("Port: "+myUrl.getPort());
            System.out.println("Athority of the URL: "+myUrl.getAuthority());
            System.out.println("Query: "+myUrl.getQuery());
            System.out.println("Reference: "+myUrl.getRef());
        } catch (MalformedURLException ex) {
            ex.printStackTrace();
        }
    }
}

