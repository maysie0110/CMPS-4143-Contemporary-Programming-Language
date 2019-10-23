import java.util.Scanner;
// May Trinh 
// This program will randomly generate an integer between 1 and 100. And will let the user guess the number. Each time the user guess it wrong, the program will give a hint whether the guessed is higher or lower than the number. 

class Main {
  public static void main(String args[]) 
    {       
      System.out.print("May Trinh.\nThis program will randomly generate an integer between 1 and 100. And will let the user guess the number. Each time the user guess it wrong, the program will give a hint whether the guessed is higher or lower than the number.\n");
      
      // Generating random double between 1-100
      int randNum = (int)(Math.random()*100 + 1);

      Scanner input = new Scanner(System.in);
    	System.out.print("I am thinking of a number between 1 and 100. Try to guess the number: ");
    	int number = input.nextInt(); //take user's input
      int count = 1; //keep count of number of guesses made
      while (number != randNum){ // keep taking user's input until they guess it right
        if(number > randNum){
          System.out.print("Lower! ");
        }
        else if (number < randNum){
          System.out.print("Higher! ");
        }
        System.out.print("Guess again: ");
    	  number = input.nextInt();
        count ++;
      }
      System.out.print("You guessed the number in "+count+" tries.");
  } 
}
