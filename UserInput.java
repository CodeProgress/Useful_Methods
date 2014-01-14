import java.util.Scanner;

public class UserInput {

	public static void main(String[] args) {
		//Tutorial for handling input
		//Create scanner object
		Scanner input = new Scanner(System.in);
		
		//Output the prompt
		System.out.println("Enter a Line of text");
		
		//Wait for the user to enter a line of text
		String line = input.nextLine();
		
		//Tell them what they entered.
		System.out.println("You entered: " + line);
		
		//All steps together, now with ints:
		Scanner input2 = new Scanner(System.in);
		System.out.println("Enter an integer");
		int value = input2.nextInt();
		System.out.println("You entered: " + value);
		
		//close the inputs
		input.close();
		input2.close();
	}

}
