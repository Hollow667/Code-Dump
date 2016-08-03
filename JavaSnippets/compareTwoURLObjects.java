import java.net.MalformedURLException;
import java.net.URL;
 
public class MyUrlCompare {
 
    public static void main(String a[]){
        try {
            URL mysite = new URL("http://www.java2novice.com");
            URL google = new URL("http://www.google.com");
            if(mysite.equals(google)){
                System.out.println("Both sites are equal");
            } else {
                System.out.println("Both sites are not equal");
            }
        } catch (MalformedURLException ex) {
            ex.printStackTrace();
        }
    }
}

