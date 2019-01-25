
class Calculator {
    int left, right;
 
    public Calculator(int left, int right){
    	this.left = left;
    	this.right = right;
    }
    
    public int sum(){
    	return this.left + this.right;
    }
}
 

class SubCalculator extends Calculator{
	public SubCalculator(int left, int right) {
		super(left, right);
	}

	public int substract(){
		return this.left - this.right;
	}
}

public class calculatorDemo {
	
	public static void main(String[] args) {
		SubCalculator c1 = new SubCalculator(10, 20);
		System.out.println(c1.sum());
		System.out.println(c1.substract());
		
	}

}
