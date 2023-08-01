public class testy{
    public static void main(String[] args) {
        int stake = Integer.parseInt(args[0]);
        int goal = Integer.parseInt(args[1]);
        int trials = Integer.parseInt(args[2]);
        int wins = 0;
        while (trials > 0){
            int cash = stake;
            while (cash > 0 && cash < goal){
                if (Math.random() < 0.5) cash++;
                else cash--;
            }
            if (cash == goal) wins++;
            trials--;
        }
        System.out.println(wins + " wins of " + trials);
    }
}