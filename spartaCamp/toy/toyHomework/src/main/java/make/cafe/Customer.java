package make.cafe;

public class Customer {
    CafeMenu customerBeverage = new CafeMenu();
//    CafeStaff cafeEmployee = new CafeStaff();



    String name ;
    int custoMermoney ;



//    메뉴 주문
    // 파라미터에 누구한테 데이터를 넘겨줄것인지도 써야한다~~ 꼭꼭 기억해
    // 객체는 독립적이어야 한다.!
    // 객체를 사용할때마다 새로 만들면 안된다..! 파라미터로 넘겨줘야 함..!
    public void orderBeverage(String name,CafeStaff employee) {
        customerBeverage.beverageMenu();
        System.out.println("고객님이 주문을 합니다.");
        System.out.println("고객 : "+ name +" 주세요..!");
        //직원한테 주문목록 전달
        employee.makeBeverage(name);
    }


//    토핑추가
    public void orderTopping(String name,CafeStaff employee) {
        customerBeverage.toppingMenu();
        System.out.println("고객님이 토핑을 추가하길 원합니다.");
        System.out.println("고객 :" + name + "추가 해주세요..!");
        //직원에게 주문 목록 전달

    }



    //돈 결제
}
