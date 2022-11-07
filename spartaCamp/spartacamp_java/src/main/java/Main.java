import java.awt.*;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int score = sc.nextInt();

        if(score > 90 && score <= 100 ){
            System.out.println("A등급 입니다.");
        } else if (score > 80 && score <= 90) {
            System.out.println("B등급 입니다.");
        } else if (score > 70 && score <= 80) {
            System.out.println("C등급 입니다.");
        }else {
            System.out.println("F등급 입니다.");
        }

        //문제 숫자를 입력받으면 입력받은 점수가 무슨 등급인지 출력
        //91-100 까지는 A등급
        //81-90 까지는 B
        //71-80 까지는 C
        // 그 외의 점수는 F등급...
    }
}