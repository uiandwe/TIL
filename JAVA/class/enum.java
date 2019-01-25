
enum Fruit{
    APPLE, PEACH, BANANA;
}
enum Company{
    GOOGLE, APPLE, ORACLE;
}


interface FRUIT1{
    int APPLE=1, PEACH=2, BANANA=3;
}
interface COMPANY1{
    int GOOGLE=1, APPLE=2, ORACLE=3;
}


public class enumDemo {

	public static void main(String[] args) {
		Fruit type = Fruit.APPLE;
        switch(type){
            case APPLE:
                System.out.println(57+" kcal");
                break;
            case PEACH:
                System.out.println(34+" kcal");
                break;
            case BANANA:
                System.out.println(93+" kcal");
                break;
        }
        
        
        int type1 = 1;
        switch(type1){
            case FRUIT1.APPLE:
                System.out.println(57+" kcal");
                break;
            case FRUIT1.PEACH:
                System.out.println(34+" kcal");
                break;
            case FRUIT1.BANANA:
                System.out.println(93+" kcal");
                break;
        }
        
	}

}
