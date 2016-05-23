import java.util.Date;
import java.text.*;

public class Date_time {

	public static void main(String[] args) {
		Date date = new Date();
		System.out.println(date.toString());
		System.out.println(date.getTime());
		System.out.println(date.getMonth());
		System.out.println(date.getYear());
		System.out.println(date.getDay());
		System.out.println(date.getHours());
		
		SimpleDateFormat sdf = new SimpleDateFormat("E yyyy/MM/dd HH:mm:ss");
		System.out.println(sdf.format(date));
	}
}
