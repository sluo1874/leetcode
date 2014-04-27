package solution;

import java.util.HashSet;
import java.util.Set;

public class Solution {

	/**
	 * @param args
	 */
	public int longestConsecutive(int[] num) {
	    if(num == null)
	        return 0;

	    Set<Integer> set = new HashSet<Integer>();
	    int max = 1;

	    for (int n : num)
	        set.add(n);

	    for (int n : num) {
	        int count = 1, i = 0;

	        while (set.contains(n - ++i)) {
	            count ++;
	            set.remove(n - i);
	        }

	        i = 0;
	        while (set.contains(n + ++i)) {
	            count ++;
	            set.remove(n + i);
	        }

	        max = Math.max(count, max);
	    }

	    return max;
	    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution s = new Solution();
		System.out.println(s.longestConsecutive(new int[]{100, 4, 200, 1, 3, 2}));
	}

}
