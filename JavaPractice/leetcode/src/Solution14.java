import java.util.Arrays;

public class Solution14 {
    public String longestCommonPrefix(String[] strs) {
        int shortestLength = Arrays.stream(strs).mapToInt(String::length).min().orElse(0);

        if (strs.length == 1) return strs[0];

        for (int j = 0; j < shortestLength; j++) {
            for (int i = 1; i < strs.length; i++) {
                if (strs[0].charAt(j) != strs[i].charAt(j)) {
                    return strs[0].substring(0, j);
                }
            }
        }
        return strs[0].substring(0, shortestLength);
    }
}
