
public class TimeIt {
	
	public static void main(String[] args) {
		
		long startTime = System.nanoTime();
		
		//Run something to time here
		
		long timeInNano = System.nanoTime() - startTime;
		
		double timeInSeconds = timeInNano * Math.pow(10, -9);
		
		System.out.println("Elapsed time in seconds: " + timeInSeconds);
		
	}
}
