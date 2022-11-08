import java.awt.*;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int sumOdd = 0;
        int sumEven = 0;
        for (int i = 0; i < 30; i++) {
            int value = i + 1;
            if (value % 2 == 0) {
                sumEven += value;

            } else {
                sumOdd += value;

            }

        }
        System.out.println("짝수의 합 :" + sumOdd);
        System.out.println("홀수의 합 :" + sumEven);

    }
}