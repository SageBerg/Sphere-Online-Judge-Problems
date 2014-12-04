/*
SPOJ 3410: Feynman
Sage Berg
3 Dec 2014
*/

import java.io.*;
import java.util.Scanner;

public class spoj3410 {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);    
    String str = ""; //string must be initialized for comparison
    int n;
    while (0 != str.compareTo("0")) {
      str = scanner.next();
      if (0 != str.compareTo("0")) {
        n = Integer.parseInt(str);
        squares(n);
      }
    }
    scanner.close();
  }

  public static void squares(int n) {
    int acc = 0;
    for (int i = 1; i < n + 1; i++) {
      acc += Math.pow(i, 2);
    }
    System.out.println(acc);
  }

}
