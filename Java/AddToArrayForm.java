import java.util.*;
public class AddToArrayForm {
    public static void main(String[] args) {
        int[] nums = {9,9,9,9,9,9,9,9,9,9};
        List<Integer> res = addToArrayForm(nums, 1);

        for(int n : res){
            System.out.println(n);
        }
    }

    public static List<Integer> addToArrayForm(int[] num, int k) {
        List<Integer> num2 = new ArrayList<>();
        List<Integer> res = new ArrayList<>();

        Stack<Integer> stack = new Stack<>();
        while(k > 0){
            stack.add(k % 10);
            k /= 10;
        }
        while(!stack.isEmpty()){
            num2.add(stack.pop());
        }

        int i = num.length - 1; int j = num2.size() - 1;
        int sum = 0; int carry = 0;
        while(i >= 0 || j>= 0){
            if(i>=0)
                sum+=num[i--];
            if(j>=0)
                sum+= num2.get(j--);
            sum+= carry;
            carry = sum>=10 ? 1 : 0;
            res.add(sum % 10);
            sum = 0;
        }

        if(carry == 1) res.add(1);

        Collections.reverse(res);


        return res;
    }
}
