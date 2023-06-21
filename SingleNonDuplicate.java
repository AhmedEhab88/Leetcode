public class SingleNonDuplicate {
    public static void main(String[] args) {
        int[] nums = {1,1,2};
        SingleNonDuplicate obj = new SingleNonDuplicate();
        int res = obj.singleNonDuplicate(nums);
        System.out.println(res);
    }

    public int singleNonDuplicate(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        int rightSize;
        boolean sameRight = false;
        boolean sameLeft = false;
        int leftSize;
        int mid;
        int result = -1;

        while (start <= end) {
            mid = (start + end) / 2;
            rightSize = end - mid;
            leftSize = mid - start;
            if (mid<nums.length-1 && nums[mid + 1] == nums[mid]) {
                rightSize--;
                sameRight = true;
            } else if (mid > 0 && nums[mid - 1] == nums[mid]) {
                leftSize--;
                sameLeft = true;
            } else {
                result = nums[mid];
                break;
            }

            if (rightSize % 2 != 0) {
                start = mid + 1;
                if (sameRight) start++;
            } else if (leftSize % 2 != 0) {
                end = mid - 1;
                if (sameLeft) end--;
            }
            sameRight = false;
            sameLeft = false;
        }

        return result;
    }
}
