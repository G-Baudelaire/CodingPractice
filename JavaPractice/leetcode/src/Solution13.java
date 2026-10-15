import java.util.HashMap;

public class Solution13 {
    public int romanToInt(String s) {
        int total = 0;
        int buffer = 0;

        int previousValue = 0;
        for (int i = 0; i < s.length(); i++) {
            int currentValue = characterMapping(s.charAt(i));
            System.out.println(currentValue);
            if (currentValue < previousValue) {
                total += buffer;
                buffer = currentValue;
            } else if (currentValue == previousValue) {
                buffer += currentValue;
            } else {
                buffer = currentValue - previousValue;
            }
            previousValue = currentValue;
        }
        total += buffer;
        return total;
    }

    private int characterMapping(Character c) {
        switch (c) {
            case 'I':
                return 1;
            case 'V':
                return 5;
            case 'X':
                return 10;
            case 'L':
                return 50;
            case 'C':
                return 100;
            case 'D':
                return 500;
            case 'M':
                return 1000;
        }
        return 10000000;
    }
}
