public class JumpGame {
    public static void main(String[] args) {
        int[] nums = {3,2,1,0,4};
        boolean res = canJump(nums);
        System.out.println(res);
    }
    public static boolean canJump(int[] nums) {
        int goal = nums.length - 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            if(i + nums[i] >= goal)
                goal = i;
        }
        return goal == 0;
    }
}
