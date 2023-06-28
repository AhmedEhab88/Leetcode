public class SearchInRotatedArray {
    public static void main(String[] args) {
        int[] test = {3,1};
        int target = 1;

        SearchInRotatedArray obj = new SearchInRotatedArray();
        int res = obj.search(test, target);
        System.out.println(res);
    }

    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        int mid;
        while (start <= end) {
            mid = (start + end) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[start] < nums[mid]) {
                if (target > nums[mid] || target <= nums[start]) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            } else {
                if (target < nums[mid] || target >= nums[end]) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            }
        }

        return -1;
    }
}
