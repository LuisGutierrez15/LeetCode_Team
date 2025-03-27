package Java;

public class Problem2 {
    public int minPatches(int[] nums, int n) {
        int count = 0, i = 0;
        long missing = 1;
        while (missing <= n) {
            if (i < nums.length && nums[i] <= missing) {
                missing += nums[i];
                i++;
            } else {
                missing += missing;
                count++;
            }

        }
        return count;
    }
}
