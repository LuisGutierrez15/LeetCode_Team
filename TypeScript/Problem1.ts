function maxProfit(prices: number[]): number {
	let n = prices.length;

    if(n < 2) return 0;

    let max_profit_left = new Array(n).fill(0);
    let min_val = prices[0];

    // Best time to buy
    for(let i = 1; i < n; i++) {
        min_val = Math.min(min_val, prices[i]);
        max_profit_left[i] = Math.max(max_profit_left[i-1], prices[i] - min_val);
    }

    let max_profit_right = new Array(n).fill(0);
    let max_val = prices[n-1];

    // Best time to sell
    for(let i = n-2; i >= 0; i--) {
        max_val = Math.max(max_val, prices[i]);
        max_profit_right[i] = Math.max(max_profit_right[i+1], max_val - prices[i]);
    }

    let best_profit = 0;
    for(let i = 0; i < n; i++) {
        best_profit = Math.max(best_profit, max_profit_left[i] + max_profit_right[i]);
    }

    return best_profit;
};