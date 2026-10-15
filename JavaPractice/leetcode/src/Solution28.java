public class Solution28 {
    public int strStr(String haystack, String needle) {
        return haystack.indexOf(needle);
//        if (needle.length() > haystack.length()) return -1;
//
//        for (int i = 0; i < haystack.length() - needle.length() + 1; i++) {
//            if (haystack.substring(i, i + needle.length()).equals(needle)) return i;
//        }
//        return -1;
    }
}
