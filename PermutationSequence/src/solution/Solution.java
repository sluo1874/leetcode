package solution;

import java.util.HashSet;
import java.util.Set;

public class Solution {

	/**
	 * @param args
	 */
	public String getPermutation(int n, int k) {
		StringBuffer sb = new StringBuffer();
		int section = 0;
		int fac = 0;
		Set<Integer> preInt = new HashSet<Integer>();
		for(int i=1; i<=n;++i) {
			fac = this.factorial(n - i);
			section = k / fac + 1;
			if( k% fac == 0) section--;
			k = k % fac;
			if (0 == k) k = fac;
			int num = this.findNum(preInt, section);
			sb.append(num);
			preInt.add(num);
		}
		return sb.toString();
	}
	private int factorial(int n) {
		int res = 1;
		for(int i = 1; i <= n; ++i){
			res*=i;
		}
		return res;
	}
	
	private int findNum(Set<Integer> preInt, int m) {
		for (int i=1; i <= 9; ++i) {
			if(preInt.contains(i) && i <= m) ++m;
		}
		return m;
		
	}
	public static void main(String[] args) {
		Solution s = new Solution();
		System.out.println(s.getPermutation(3, 6));
	}

}
