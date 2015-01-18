import java.io.*;
import java.util.Scanner;
import java.util.Arrays;

class FashionShows {

  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    int trials = Integer.parseInt(scanner.nextLine());
    while (trials > 0) {
      int couples = Integer.parseInt(scanner.nextLine());
      String[] men = scanner.nextLine().split(" ");
      String[] women = scanner.nextLine().split(" ");
      Arrays.sort(men); 
      Arrays.sort(women); 
      int hotness = 0;
      for (int i = 0; i < couples; i++) {
        hotness += Integer.parseInt(men[i]) * 
                   Integer.parseInt(women[i]);
      }
      System.out.println(hotness);
      trials -= 1;
    }
  }

}
