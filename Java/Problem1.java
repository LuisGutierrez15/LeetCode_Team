package Java;

public class Problem1 {

    public int max(int a, int b) {
        return a > b ? a : b;
    }

    public int min(int a, int b) {
        return a < b ? a : b;
    }

    public int maxProfit(int[] prices) {
        int n = prices.length;

        if (n < 2) {
            return 0;
        }

        int[] maxProfitLeft = new int[n];
        for (int i = 0; i < n; i++) {
            maxProfitLeft[i] = 0;
        }
        int minVal = prices[0];

        for (int i = 1; i < n; i++) {
            minVal = min(minVal, prices[i]);
            maxProfitLeft[i] = max(maxProfitLeft[i - 1], (prices[i] - minVal));
        }

        int[] maxProfitRigth = new int[n];
        for (int i = 0; i < n; i++) {
            maxProfitRigth[i] = 0;
        }
        int maxVal = prices[n - 1];

        for (int i = n - 1; i > 0; i--) {
            maxVal = max(maxVal, prices[i]);
            maxProfitRigth[i] = max(maxProfitRigth[i - 1], (maxVal - prices[i]));
        }

        int bestProfit = 0;

        for (int i = 0; i < n; i++) {
            bestProfit = max(bestProfit, maxProfitLeft[i] + maxProfitRigth[i]);
        }

        return bestProfit;
    }
}
