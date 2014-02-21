import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.TreeMap;

public class MiscMaps {
	
	public static void main(String[] args){
		int x;
		double sq;
		
		ArrayList<Integer>             arr = new ArrayList<Integer>();
		HashMap<Integer, Double>        hm = new HashMap<Integer, Double>();
		TreeMap<Integer, Double>        tm = new TreeMap<Integer, Double>();
		LinkedHashMap<Integer, Double> lhm = new LinkedHashMap<Integer, Double>();
		
		for (int i = 0; i < 10; i++){
			x = (int) (Math.random()*10);
			sq = x * x;
			arr.add(x);
			hm.put(x, sq);
			tm.put(x, sq);
			lhm.put(x, sq);
			
		}
		
		System.out.println("array: " + "\t" + "\t" + arr.toString());
		System.out.println("HashMap: "      + "\t" + hm.toString());
		System.out.println("TreeMap: "      + "\t" + tm.toString());
		System.out.println("LinkedHashMap:" + "\t" + lhm.toString());

	}

}


