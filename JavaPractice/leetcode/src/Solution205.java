public class Solution205 {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] mapS = new int[256];
        int[] mapT = new int[256];

        for (int i = 0, n = s.length(); i < n; i++) {
            char c1 = s.charAt(i);
            char c2 = t.charAt(i);

            if (mapS[c1] != mapT[c2]) {
                return false;
            }

            mapS[c1] = i;
            mapT[c2] = i;
        }

        return true;
    }
}
