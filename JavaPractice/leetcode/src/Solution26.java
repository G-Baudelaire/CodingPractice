import java.util.Arrays;

public class Solution26 {
    public int removeDuplicates(int[] nums) {
        if (nums.length < 2) return nums.length;

        int write = 1;
        for (int read = 1; read < nums.length; read++) {
            if (nums[read] != nums[read - 1]) nums[write++] = nums[read];
        }

        return write;
    }
}
