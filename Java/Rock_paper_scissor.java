import java.util.Scanner;
public class Rock_paper_scissor {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        if(a.equals("rock")){
            System.out.println("Paper");
        }else if(a.equals("scissor")){
            System.out.println("Rock");
        }else if(a.equals("paper")){
            System.out.println("Scissor");
        }sc.close();
        
        }
    }

