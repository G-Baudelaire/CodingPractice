public class Solution27 {
    public int removeElement(int[] nums, int val) {
        if (nums.length == 0) return 0;
        int write = 0;
        for (int num : nums) {
            if (num != val) {
                nums[write++] = num;
            }
        }
        return write;
    }
}
