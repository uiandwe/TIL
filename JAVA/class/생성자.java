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
 

public class calculatorDemo {
	
	public static void main(String[] args) {
		Calculator c1 = new Calculator(10, 20);
		System.out.println(c1.sum());
	}

}
