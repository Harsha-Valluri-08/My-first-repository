import java.util.Scanner;

public class Harsha {
    public static void main(String[] args){
        System.out.print("Enter your name: ");
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println("Hello, "+s);
        sc.close();
    }
}
