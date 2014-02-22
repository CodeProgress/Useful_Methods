import java.util.ArrayList;

public class Sieve {
	
	public static void main(String[] args){
		ArrayList<Integer> x = sieve(1000000);
		System.out.println(x.size());
	} 
	
	public static ArrayList<Integer> sieve(int limit){
		ArrayList<Integer> primes = new ArrayList<Integer>();
		
		if (limit < 2){
			return primes;
		}
		
		boolean[] primeBools = new boolean[limit + 1];
		
		for (int i = 2; i < limit+1; i++){
			if (primeBools[i] != true){
				primes.add(i);
				primeBools[i] = true;
				for (int j = i*2; j < limit +1; j += i){
					primeBools[j] = true;
				}
			}
		}
		
		return primes;
		
	}

}
