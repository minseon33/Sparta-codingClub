package org.example;

public class CarExample {
    public static void main(String[] args){
        //객체생성
        Car myCar = new Car();

        //필드 값 읽기
        System.out.println("제작회사:" + myCar.company);
        System.out.println("모델명:" + myCar.model);
        System.out.println("색깔:"+ myCar.color);
        System.out.println("최고 속도:" + myCar.maxSpeed);
        System.out.println("현재 속도:" + myCar.speed);

        //필드값 변경
        myCar.speed = 60;
        System.out.println("수정된 속도:" + myCar.speed);

        // 질문..! 객체가 생성된건.. 객체가 복사된거니까.. myCar.speed = 60; 로 스피드값 바꿔도 car클래스의 데이터는 영향이 없는건가...?
        // 근데 car 클래스의 제어자가 private라면..? -> 해봤는데 에러나네.. 그래서 바꿔야할 때 프라이빗 풀어주라고 했던거구나..

    }
}
