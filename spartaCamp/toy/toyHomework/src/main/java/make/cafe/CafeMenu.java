package make.cafe;


import java.util.HashMap;

public class CafeMenu {

    String name;

    CafeMenu(){
    }

    HashMap<String, Integer> beverage = new HashMap<String, Integer>();
    HashMap<String, Integer> topping = new HashMap<String, Integer>();

    // 음료 메뉴
    public void beverageMenu() {

        beverage.put("americano", 1000);

        beverage.put("cafeLatte", 1500);

        beverage.put("milkTea", 2000);

        beverage.put("milkShake", 3000);

        beverage.put("chamomile", 4000);

    }
    //토핑 메뉴
    public void toppingMenu() {
        topping.put("shot", 500);

        topping.put("whippingCream", 1000);

        topping.put("milk", 1500);

        topping.put("none",0);
    }


    //음료메뉴 보여주기
    public void showBeverageMenu(){
        for (String i : beverage.keySet()) {

            System.out.println(i + " : " + beverage.get(i));

        }


    }

    //고객이 고른메뉴 보여주기


    //토핑메뉴 보여주기
    public void showToppingMenu(){
        for (String i : topping.keySet()) {

            System.out.println(i + " : " + topping.get(i));
        }
    }

}
