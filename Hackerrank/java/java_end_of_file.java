// https://www.hackerrank.com/challenges/java-end-of-file/problem
// Java End Of File

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);
        int i = 1;
        while(scanner.hasNext()){
            System.out.printf("%d %s%n",i,scanner.nextLine());
            i++;
        }
        scanner.close();
    }
}