import java.util.Scanner;

public class AppendExample {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first string: ");
        String str1 = sc.nextLine();

        System.out.print("Enter second string to append: ");
        String str2 = sc.nextLine();

        StringBuilder sb = new StringBuilder(str1);
        sb.append(str2);

        System.out.println("After appending: " + sb.toString());
    }
}

