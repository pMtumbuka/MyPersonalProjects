import java.security.Principal;
import java.text.NumberFormat;
import java.util.Scanner;

public class Calculator{

public static void main(String pmm[]) {
	
	final byte MONTHS_IN_YEAR = 12;
        final byte PERCENT = 100;

        Scanner Scan = new Scanner(System.in);

        System.out.print("Principal: ");
        float principal = Scan.nextInt();
        if (principal >= 1000 && principal <= 1000000)
            System.out.println(principal);
        else
            System.out.println("Please Enter A Number Between 1,000 And 1,000,000.");
                continue;
        float x = principal;

        System.out.print("Annual Interest Rate: ");
        float annualInterest = Scan.nextFloat();
        float monthlyInterest = annualInterest / MONTHS_IN_YEAR / PERCENT;
        float y = monthlyInterest;

        System.out.print( "Period (Years): ");
        byte years = Scan.nextByte();
        float numberOfPayments = years * MONTHS_IN_YEAR;
        byte z = years;

        double mortgage = principal * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments) / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1));

        String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);


        System.out.println("Mortgage: " + mortgageFormatted );

		
}	
}