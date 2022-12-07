
import java.util.HashMap;
public class test {
    public static void main(String[] args) {
        HashMap<String, String> codes = new HashMap<String, String>();

        codes.put("HTML", "뼈대");

        codes.put("CSS", "디자인");

        codes.put("JS", "기능");

        codes.put("SQL", "DB");

        for (String i : codes.keySet()) {

            System.out.println( i + " : " + codes.get(i));

        }
    }
}



