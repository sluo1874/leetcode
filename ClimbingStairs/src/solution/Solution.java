package solution;

public class Solution {

	/**
	 * @param args
	 */
	public int climbStairs(int n) {
		int[] ways = new int[n + 1];
		ways[0] = 1;
		ways[1] = 1;
		for(int i = 2; i<=n; i++) {
			ways[i] = ways[i-2] + ways[i-1];
		}
		return ways[n];
    }
	public static void main(String[] args) {
		Solution so = new Solution();
		System.out.println(so.climbStairs(2));
	}

}
