import java.util.Date;
import java.util.Calendar;

public class MyClass {

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        
        System.out.println("-------------------");

        // 1.) Using the "Date" Class in the "java.util" package 

        Date todaysDate = new Date();

        System.out.println(todaysDate.toString());

        System.out.println(todaysDate.getTime());

        System.out.println(todaysDate.getMonth() + 1);

        System.out.println(todaysDate.getHours());

        System.out.println(todaysDate.getYear() + 1900);

        System.out.println(todaysDate.getDay());

        System.out.println("---------------------");

        // 2.) Using the "Calendar" Class in the "java.util" package

        Calendar rightNow = Calendar.getInstance();

        System.out.println(rightNow.getTime());

        System.out.println(rightNow.getWeekYear());

        System.out.println(rightNow.getWeeksInWeekYear());

        System.out.println(rightNow.getTimeZone());

       // System.out.println(rightNow.toString());

       System.out.println("----------------------");

    }
       
}

      