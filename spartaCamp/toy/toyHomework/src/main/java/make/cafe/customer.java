package make.cafe;

public class customer {
    cafeMenu customerBeverage = new cafeMenu();


    String name;

    customer() {
    }


    //    customer(String beverageName, int beveragePrice ){
//        this.beverageName = beverageName;
//        this.beveragePrice = beveragePrice;
//
//    }
//    customer(String toppingName, int toppingPrice){
//        this.toppingName = toppingName;
//        this.toppingPrice = toppingPrice;
//
//    } >> 이거 오버로딩 아님;

    public void putBeverage(String name) {
        customerBeverage.beverageMenu();
        System.out.println("고객이 주문함");
        System.out.println(name + ":" + customerBeverage.beverage.get(name));


    }

    public void putTopping(String name) {
        customerBeverage.toppingMenu();
    }
}
