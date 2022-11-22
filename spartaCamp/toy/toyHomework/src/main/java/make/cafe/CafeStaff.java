package make.cafe;

public class CafeStaff {
    CafeMenu cafeBeverage = new CafeMenu();
    String makeName;

    public void makeBeverage(String madeName) {
        cafeBeverage.beverageMenu();
        System.out.println("Staff: 주문하신 "+ madeName + " 음료를 제작합니다.");
        System.out.println(".");
        System.out.println(".");
        System.out.println(".");
        System.out.println("Staff: 주문하신 " + madeName + " 음료 나왔습니다. ");
    }

}
