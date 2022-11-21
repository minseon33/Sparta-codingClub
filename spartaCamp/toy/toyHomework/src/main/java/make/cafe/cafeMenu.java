package make.cafe;


import java.util.HashMap;

public class beverageMenu {

    HashMap<String, String> beverage = new HashMap<String, String>();

    public void showMenu() {

        beverage.put("americano", "1000");

        beverage.put("cafeLatte", "1500");

        beverage.put("milkTea", "2000");

        beverage.put("milkShake", "3000");

        beverage.put("chamomile", "4000");

        for (String i : beverage.keySet()) {

            System.out.println(i + " : " + beverage.get(i));

        }
    }

    public void showTopping() {
        beverage.put("샷추가", "500");

        beverage.put("휘핑크림 추가", "1000");

        beverage.put("우유 추가", "1500");

        for (String i : beverage.keySet()) {

            System.out.println(i + " : " + beverage.get(i));

        }
    }
    public static void main(String[] args) {


    }


}
