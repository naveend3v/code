// https://www.hackerrank.com/challenges/java-string-compare/problem
// Java SubString Comparison

import java.util.Scanner;

// Change below class name "java_substring_comparisons" to "Solution" when running this code in HackerRank submission
public class java_substring_comparisons {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";

        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'

        smallest = s.substring(0, k);
        largest = s.substring(0, k);

        for(int i=0;i<=s.length()-k;i++){
            String subString = s.substring(i,i+k);

            if(subString.compareTo(smallest)<0){
                smallest= subString;
            }

            if(subString.compareTo(largest)>0){
                largest = subString;
            }
        }

        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}