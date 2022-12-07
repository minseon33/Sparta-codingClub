package make.cafe;

public class Main {
    public static void main(String[] args) {

//        직원 고용
        CafeStaff partTimeEmployee = new CafeStaff();

        //카페 오픈
        // Show me the menu
        CafeMenu d = new CafeMenu();
        System.out.println("---------<메뉴판>-------");
        d.beverageMenu();
        d.showBeverageMenu();
        System.out.println("--------<토핑추가>------");
        d.toppingMenu();
        d.showToppingMenu();
        System.out.println("=======================");
        //고객 입장~

        System.out.println("<고객 입장>");
        Customer cafeCustomer = new Customer();
        //고객 주문
        cafeCustomer.orderBeverage("americano","shot", partTimeEmployee);

//        고객 돈 지불
        cafeCustomer.beveragePayment(5000);

//        손님이 주문한거 직원이 넘겨받고 음료 제작 고~!


    }
}