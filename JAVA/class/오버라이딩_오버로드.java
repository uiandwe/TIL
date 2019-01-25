
class Calculator {
    int left, right;
    int third = 0;
    
    public Calculator(int left, int right){
    	this.left = left;
    	this.right = right;
    }
    
    public int sum(){
    	return this.left + this.right;
    }
    
    public int sum(int third){
        return this.left + this.right + third;
    }
}
 

class SubCalculator extends Calculator{
	public SubCalculator(int left, int right) {
		super(left, right);
	}

	public int substract(){
		return this.left - this.right;
	}
	
	public int sum(){
		 System.out.println("실행 결과는 " +(this.left + this.right)+"입니다.");
		 return 0;
	}
}

class MultiplicationCalculator extends SubCalculator{

	public MultiplicationCalculator(int left, int right) {
		super(left, right);
	}
	
	public int mul(){
		return this.left * this.right;
	}
	
}

public class calculatorDemo {
	public calculatorDemo(){}
    public calculatorDemo(int param1) {}
	public static void main(String[] args) {
		
		calculatorDemo  c = new calculatorDemo();
		
		SubCalculator c1 = new SubCalculator(10, 20);
		System.out.println(c1.sum());
		System.out.println(c1.sum(1));
		System.out.println(c1.substract());
		
		
		MultiplicationCalculator m1 = new MultiplicationCalculator(10, 20);
		System.out.println(m1.sum());
		System.out.println(m1.substract());
		System.out.println(m1.mul());
		
	}

}
