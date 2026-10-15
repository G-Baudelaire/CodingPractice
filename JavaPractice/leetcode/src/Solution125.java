public class Solution125 {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();

        int left_pointer = 0;
        int right_pointer = s.length() - 1;

        while (left_pointer < right_pointer) {
            while (left_pointer < right_pointer && !Character.isLetterOrDigit(s.charAt(left_pointer))) left_pointer++;
            while (left_pointer < right_pointer && !Character.isLetterOrDigit(s.charAt(right_pointer))) right_pointer--;
            if (s.charAt(left_pointer) != s.charAt(right_pointer)) return false;
            left_pointer++;
            right_pointer--;
        }

        return true;
    }
}
