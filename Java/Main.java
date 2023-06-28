class Main {

    public static boolean isHappy(int n) {
        int slow, fast;
        slow  = n;
        fast = powerOfDigits(n);

        do {
            slow = powerOfDigits(slow);
            fast = powerOfDigits(powerOfDigits(fast));
        } while(slow != fast);

        return slow == 1;

    }

    private static int powerOfDigits(int n){
        int sum = 0;
        while(n != 0){
            sum += (n%10) * (n%10);
            n /= 10;
        }
        return sum;
    }

//    public static boolean isHappy(int n) {
//        int s=0;
//        System.out.println("n:"+ n);
//        while(n>0){
//            int a = n%10;
//            s += a*a;
//            n /=10;
//        }
//        System.out.println(" s: " + s);
//        if(s == 1) return true;
//        else if(s == 4) return false;
//        return isHappy(s);
//    }
    public static void main(String[] args)
    {
        boolean check = isHappy(99);
        System.out.println(check);
    }
}