package Java;

import java.lang.Math;

public class Problem3 {

    public String shortestPalindrome(String s) {
        if (s.isEmpty()) {
            return s;
        }

        String sMirror = new StringBuffer(s).reverse().toString();

        int step = 0;
        while (true) {
            String test = s;
            String temp = new StringBuffer(test).substring(0, step).toString();

            test = temp + test;

            boolean isOdd = test.length() % 2 == 1;
            int pivot = isOdd ? Math.ceilDiv(test.length(), 2) : test.length() / 2;
            pivot -= 1;

            String firstPart = new StringBuffer(test).substring(0, pivot).toString();
            String firstReversed = new StringBuffer(firstPart).reverse().toString();
            String secondPart = new StringBuffer(test).substring(pivot).toString();

            System.out.println(firstReversed);
            System.out.println(secondPart);

            if (firstPart.equalsIgnoreCase(secondPart)) {
                return test;
            }

            step++;

        }

    }

}
