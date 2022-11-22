package make.cafe;


import java.sql.SQLOutput;
import java.util.HashMap;

public class cafeMenu {

    String name;

    cafeMenu(){
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
        topping.put("샷추가", 500);

        topping.put("휘핑크림 추가", 1000);

        topping.put("우유 추가", 1500);
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
