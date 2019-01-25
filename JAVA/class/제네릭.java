
interface Info{
    int getLevel();
}

class EmployeeInfo implements Info{
	public int rank;
	EmployeeInfo(int rank){
		this.rank = rank;
	}
	public int getLevel(){
        return this.rank;
    }
}

class Person<T extends Info>{
	public T info;;
	
	Person(T info){
		this.info = info;
	}
	
	public <c> void printInfo(c info){
		System.out.println(info);
	}
	
}

public class GenericDemo {

	public static void main(String[] args) {
		EmployeeInfo e = new EmployeeInfo(1);
		Person<EmployeeInfo> p1 = new Person<EmployeeInfo>(e);
//		Person<Object> p2 = new Person<Object>("test");
		p1.<EmployeeInfo>printInfo(e);
		p1.printInfo(e);

	}

}
