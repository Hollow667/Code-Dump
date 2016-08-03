import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
 
public class MyURLDecode {
    public static void main(String a[]){
        try {
            System.out.println(URLDecoder.decode("special+chars%3A+%26%25*+", "UTF-8"));
        } catch (UnsupportedEncodingException ex) {
            ex.printStackTrace();
        }
    }
}

