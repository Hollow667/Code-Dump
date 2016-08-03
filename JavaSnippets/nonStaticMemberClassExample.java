public class MyBasicNonStaticMemberClass {
 
    public class ChildClass{
         
        public void myMethod(){
            System.out.println("Hey you have called me!!!");
        }
    }
     
    public ChildClass getInnerInstance(){
        return this.new ChildClass();
    }
     
    public static void main(String a[]){
        MyBasicNonStaticMemberClass mbn = new MyBasicNonStaticMemberClass();
        ChildClass cc = mbn.getInnerInstance();
        cc.myMethod();
    }
}

