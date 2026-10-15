public class Solution9 {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;

        long working_value = x;
        long reversed = 0;

        while (working_value != 0) {
            reversed *= 10;
            reversed += working_value % 10;
            working_value /= 10;
        }

        return (x == reversed);
    }
}
