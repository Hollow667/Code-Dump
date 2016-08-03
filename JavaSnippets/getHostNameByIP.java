import java.net.InetAddress;
import java.net.UnknownHostException;
 
public class MyHostName {
 
    public static void main(String a[]){
     
        try {
            InetAddress host = InetAddress.getByName("72.167.232.155");
            System.out.println(host.getHostName());
        } catch (UnknownHostException ex) {
            ex.printStackTrace();
        }
    }
}

