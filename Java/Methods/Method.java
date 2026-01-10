import java.util.Scanner;
    // In java "Method" are known as functions  ..
public class Method {
    public static void main(String[] args) {
        sum();
    }// In static functions, the static fuction need to call....
    static void sum(){
        Scanner sc = new Scanner(System.in);
        int a,b;
        System.out.print("Enter the values of a and b: ");
        a = sc.nextInt();
        b = sc.nextInt();
        System.out.println(a+b);
        sc.close();
    }
}
        // Return is nothing but is gives a value to function call variable