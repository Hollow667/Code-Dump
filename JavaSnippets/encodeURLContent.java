import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
 
public class MyUrlEncode {
 
    public static void main(String a[]){
     
        try {
            System.out.println(URLEncoder.encode("String with spaces", "UTF-8"));
            System.out.println(URLEncoder.encode("special chars: &%*", "UTF-8"));
        } catch (UnsupportedEncodingException ex) {
            ex.printStackTrace();
        }
    }
}

