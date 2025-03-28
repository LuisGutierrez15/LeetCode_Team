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
            String temp = new StringBuffer(sMirror).substring(0, step).toString();
            test = temp + test;

            boolean isOdd = test.length() % 2 == 1;
            int pivot = isOdd ? Math.ceilDiv(test.length(), 2) : test.length() / 2;

            String firstPart = new StringBuffer(test).substring(0, pivot).toString();
            String firstReversed = new StringBuffer(firstPart).reverse().toString();
            String secondPart = new StringBuffer(test).substring(isOdd ? pivot - 1 : pivot).toString();

            if (firstReversed.equalsIgnoreCase(secondPart)) {
                return test;
            }

            step++;

        }

    }
}
