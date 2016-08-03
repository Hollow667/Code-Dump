import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;
 
public class MyUrlContentRead {
 
    public static void main(String a[]){
     
        URL url = null;
        InputStream is = null;
        try {
            url = new URL("http://www.java2novice.com");
            is = url.openStream();
            byte[] b = new byte[8];
            while(is.read(b) != -1){
                System.out.print(new String(b));
            }
        }  catch (MalformedURLException ex) {
            ex.printStackTrace();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}

