import java.util.Arrays;

public class Solution121 {
    public int maxProfit(int[] prices) {
        if (prices.length <= 1) return 0;

        int[] buy = new int[prices.length];
        int[] sell = new int[prices.length];

        buy[0] = prices[0];
        for (int i = 1; i < prices.length; i++) {
            buy[i] = Math.min(prices[i], buy[i - 1]);
        }
        System.out.println(buy.toString());
        sell[sell.length - 1] = prices[prices.length - 1];
        for (int i = prices.length - 1; i > -1; i--) {
            sell[i] = Math.max(prices[i], sell[i]);
        }
        System.out.println(sell.toString());
        int best_price = sell[0] - buy[1];
        for (int i = 1; i < buy.length - 1; i++) {
            best_price = Math.max(best_price, sell[i] - buy[i + 1]);
        }
        return Math.max(best_price, 0);
    }
}
