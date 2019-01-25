interface Calculatable {
	public void setOprands(int first, int second);
	
}


class CalculatorDummy implements Calculatable{
	int first, second;
    public void setOprands(int first, int second){
    	this.first = first;
        this.second = second;
    }
    public int sum(){
    	return this.first + this.second;
    }
    public int avg(){
    	 return (this.first + this.second) / 2;
    }
}


public class InterfaceDemo {

	public static void main(String[] args) {
		CalculatorDummy c = new CalculatorDummy();
        c.setOprands(10, 20);
        System.out.println(c.sum()+c.avg());

	}

}
