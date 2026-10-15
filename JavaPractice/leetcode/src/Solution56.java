public class Solution56 {
    public int lengthOfLastWord(String s) {
        s = s.stripTrailing();
        int end = s.length() - 1;
        int last_space = s.lastIndexOf(' ');
        return end - last_space;
    }
}
