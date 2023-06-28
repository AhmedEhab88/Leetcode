import java.util.*;
public class PlusOne {
    public static void main(String[] args) {
        int[] digits = {1,0,0,0};
        int[] result = plusOne(digits);
        for(int i: result){
            System.out.println(i);
        }
    }
    public static int[] plusOne(int[] digits) {
        List<Integer> helper = new ArrayList<>(digits.length);
        int carry = 1;
        int current;

        for (int num : digits)
            helper.add(num);

        for (int i = digits.length - 1; i >= 0; i--) {
            current = (helper.get(i) + carry);
            carry = current == 10? 1 : 0;
            helper.set(i, current % 10);
        }

        if(carry == 1) helper.add(0, carry);

        int[] result = convertIntegers(helper);
        return result;
    }

    public static int[] convertIntegers(List<Integer> integers) {
        int[] ret = new int[integers.size()];
        for (int i = 0; i < ret.length; i++) {
            ret[i] = integers.get(i).intValue();
        }
        return ret;
    }
}
