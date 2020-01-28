import java.util.ArrayList;
import java.util.Collections;

public class E4 {

    public static void main(String[] args) {

        ArrayList<Integer> arrayList = new ArrayList<Integer>();

        for (int i = 999; i > 99; i--) {
            for (int j = 999; j > 99; j--) {
                int boi = (Integer.parseInt(new StringBuilder((i * j) + "").reverse().toString()));
                if ((i * j) == boi) {
                    arrayList.add(i * j);
                    System.out.println(i * j);
                }
            }
        }
        System.out.println(Collections.max(arrayList));
    }

}
