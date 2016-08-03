public class MyBasicStaticMemberClass {
 
    public static class MyStaticMemberExampleClass {
 
        public void printStatus() {
            System.out.println("Hey I am inside static member class");
        }
    }
 
    public static void main(String a[]) {
        StaticMemberTestClass smt = new StaticMemberTestClass();
        smt.testMemberClass();
    }
}
 
class StaticMemberTestClass {
 
    public void testMemberClass() {
        MyBasicStaticMemberClass.MyStaticMemberExampleClass msme
                    = new MyBasicStaticMemberClass.MyStaticMemberExampleClass();
        msme.printStatus();
    }
}

