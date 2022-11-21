package org.example;


import java.util.HashMap;

public class beverageMenu {

    HashMap<String, String> beverage = new HashMap<String, String>();

    public void showMenu() {

        beverage.put("아메리카노", "1000");

        beverage.put("카페라떼", "1500");

        beverage.put("밀크티", "2000");

        beverage.put("밀크쉐이크", "3000");

        beverage.put("캐모마일", "4000");

        for (String i : beverage.keySet()) {

            System.out.println( i + " : " + beverage.get(i));

        }
    }
    public static void main(String[] args) {
        beverageMenu d = new beverageMenu();

    }


}
