package mpoa;

import java.util.HashSet;

public class Solution {
	
	
	private HashSet<Double> lines;
	
	public Solution() {
		lines = new HashSet<Double>();
	}
	
	public int maxPoints(Point[] points) {
		int max = 0;
		for (int i = 0; i < points.length ; i++) {
			for (int j = i; j < points.length; j ++) {
				double k = calLine(points[i], points[j]);
				if (lines.contains(k)) continue;
				lines.add(k);
				int temp = 0;
				for (int n = 0; n < points.length; n++) {
					if (onLine(k, points[i], points[n])) {
						temp++;
					}
				}
				if (temp >= points.length/2) {
					max = temp;
					break;
				} else if (temp > max) {
					max = temp;
					continue;
				}
			}
			lines.clear();
		}
        return max;
    }
	
	private static double calLine(Point a, Point b) {
		double k = ((double)b.x - (double)a.x) / (b.x - a.x);
		return k;
	}
	
	private static boolean onLine(double k, Point a, Point b) {
		if(k == ((double)b.x - (double)a.x) / (b.x - a.x)) return true;
		else return false;
	}
}
