package make.cafe;

public class customer {
    cafeMenu beverage = new cafeMenu();


    String beverageName;
    int beveragePrice;
    String toppingName;
    int toppingPrice;

    customer(){
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


    public void putBeverage(String beverageName){
        beverage.beverageMenu();
        System.out.println(beverage.get(beverageName));



    }
    public void putTopping(String toppingName,int toppingPrice){
        beverage.toppingMenu();
        System.out.println( toppingName +"," + toppingPrice );

    }
}
