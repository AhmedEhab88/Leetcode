import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class AddBinary {
    public static void main(String[] args) {
        String x = "1010";
        String y = "1011";
        String res = addBinary(x, y);

        System.out.println(res);
    }

    public static String addBinary(String a, String b) {
        StringBuilder res = new StringBuilder();
        int i = a.length() - 1;
        int j = b.length() - 1;

        int carry = 0;
        int sum = 0;

        while(i>=0 || j>= 0)
        {
            if(i>=0)
                sum += (a.charAt(i--) - '0');
            if(j>=0)
                sum += (b.charAt(j--) - '0');
            sum += carry;
            carry = sum >= 2 ? 1 : 0;
            res.append(sum % 2);
            sum = 0;
        }

        if(carry == 1) res.append(carry);

        String result = res.reverse().toString();

        return result;
    }
}
