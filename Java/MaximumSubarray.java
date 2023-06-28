public class MaximumSubarray {
    public static void main(String[] args) {
        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
        int res = maxSubArray(nums);
        System.out.println(res);
    }

    public static int maxSubArray(int[] nums) {
        if(nums.length == 1) return nums[0];
        int max = Integer.MIN_VALUE;
        int sum = 0;

        for(int n: nums) {
            sum += n;
            max = Math.max(max, sum);

            if (sum < 0)
                sum = 0;
        }

        return max;
    }
}
