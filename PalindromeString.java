import java.util.Scanner;

public class PalindromeString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = sc.nextLine();
        sc.close();
        
        String reversed = "";
        
        // Reverse the string
        for (int i = str.length() - 1; i >= 0; i--) {
            reversed += str.charAt(i);
        }
        
        // Compare ignoring case
        if (str.equalsIgnoreCase(reversed)) {
            System.out.println(str + " is a palindrome.");
        } else {
            System.out.println(str + " is not a palindrome.");
        }
    }
}

