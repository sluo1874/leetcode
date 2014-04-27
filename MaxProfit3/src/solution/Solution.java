package solution;

import java.util.ArrayList;
import java.util.List;

public class Solution {

	/**
	 * @param args
	 */
	
    public int maxProfit(int[] prices) {
    	if (prices.length == 0) return 0;
        int[] history = new int[prices.length];
        int valley = prices[0];
        int peak = prices[prices.length -1];
        int maxProfit = 0;
        history[0] = 0;
        int futureMax = 0;
        for(int i = 1; i < prices.length; i++) {
        	if (valley > prices[i]) valley = prices[i];
        	history[i] = prices[i] - valley;
        	if (history[i] < history[i-1]) history[i] = history[i-1];
        }
        
        for(int i = prices.length -1; i>0; --i) {
        	if (peak < prices[i]) peak = prices[i];
        	if (futureMax < peak - prices[i]) {
        		futureMax = peak - prices[i];
        	}
        	if (maxProfit < history[i] + futureMax) {
        		maxProfit = history[i] + futureMax;
        	}
        }
    	return maxProfit;
    }
    
	public static void main(String[] args) {
		Solution s = new Solution();
		System.out.println(s.maxProfit(new int[]{1,2}));

	}

}
