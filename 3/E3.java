public class E3 {
    public static void main(String[] args) {
        long num = 600851475143L;
        System.out.println(primFak(num));
    }

    public static long primFak(long x) {
        long a = 2;
        while (x > 1) {
            if ((x % a) == 0) {
                x = x / a;
            } else {
                a++;
            }
            
        }
        return a;
    }
}
