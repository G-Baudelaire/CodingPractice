import java.util.HashMap;

public class Solution1 {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];
            if (hashMap.containsKey(difference)) {
                return new int[]{i, hashMap.get(difference)};
            } else {
                hashMap.put(nums[i], i);
            }
        }

        return null;
    }
}
