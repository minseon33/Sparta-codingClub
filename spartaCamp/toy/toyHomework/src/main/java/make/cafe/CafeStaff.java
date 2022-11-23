package make.cafe;

public class CafeStaff {
    CafeMenu cafeBeverage = new CafeMenu();
    String makeName;
    String beverageName;
    String toppingName;
    int totalBeveragePayment;


    //주문받기
    public void takeOrder(String beverageName,String toppingName){
        cafeBeverage.beverageMenu();
        cafeBeverage.toppingMenu();
        totalBeveragePayment = cafeBeverage.beverage.get(beverageName) + cafeBeverage.topping.get(toppingName);
        System.out.println("Staff: 주문하신 "+ beverageName + " 의 금액은 " + totalBeveragePayment+ " 원 입니다.");



    }



    //음료제작
    public void makeBeverage(String madeName,String toppingName) {
        cafeBeverage.beverageMenu();
        System.out.println("Staff: 주문하신 "+ madeName + " 음료를 제작합니다.");
        System.out.println("Staff: 주문하신 "+ toppingName + " 토핑을 추가합니다.");
        System.out.println(".");
        System.out.println(".");
        System.out.println(".");
        System.out.println("Staff: 주문하신 " + madeName + " 음료 나왔습니다. ");
    }

}
