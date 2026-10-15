public class Solution383 {
    public boolean canConstruct(String ransomNote, String magazine) {
        if (magazine.length() < ransomNote.length()) return false;
        int[] characterCount = new int[26];

        for (int i = 0; i < magazine.length(); i++) {
            characterCount[magazine.charAt(i) - 'a']++;
        }

        for (int i = 0; i < ransomNote.length(); i++) {
            if (--characterCount[ransomNote.charAt(i) - 'a'] < 0) return false;
        }

        return true;
    }
}
