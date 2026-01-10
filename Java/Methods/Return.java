import java.util.Scanner;

public class Return {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your named:");
        String s = sc.next();
        s = changename(s);
        System.out.print("Renamed name is "+s);
        sc.close();
    }static String changename(String c){
            c = "Harsha";
            return c;
    }
}
