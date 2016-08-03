import java.net.InetAddress;
import java.net.UnknownHostException;
 
public class MyIpByHost {
 
    public static void main(String a[]){
     
        try {
            InetAddress host = InetAddress.getByName("www.java2novice.com");
            System.out.println(host.getHostAddress());
        } catch (UnknownHostException ex) {
            ex.printStackTrace();
        }
    }
}

