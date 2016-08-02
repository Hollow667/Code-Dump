public class MySingleton {
 
    private static MySingleton myObj;
     
    static{
        myObj = new MySingleton();
    }
     
    private MySingleton(){
     
    }
     
    public static MySingleton getInstance(){
        return myObj;
    }
     
    public void testMe(){
        System.out.println("Hey.... it is working!!!");
    }
     
    public static void main(String a[]){
        MySingleton ms = getInstance();
        ms.testMe();
    }
}
- See more at: http://www.java2novice.com/java-interview-programs/java-singleton/#sthash.FvDEWj5c.dpuf
