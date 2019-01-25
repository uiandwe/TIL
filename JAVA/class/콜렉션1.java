package com.nts.test;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;

public class collection {

	public static void main(String[] args) {
		String[] arrayObj = new String[2];
		arrayObj[0] = "one";
		arrayObj[1] = "two";
		
		for (int i = 0; i < arrayObj.length; i++) {
			System.out.println(arrayObj[i]);
		}
		
		ArrayList<String> al = new ArrayList<String>();
		al.add("one");
        al.add("two");
        al.add("two");
        al.add("three");
        al.add("three");
        al.add("five");
        System.out.println("\narray");
        Iterator<String> ai = al.iterator();
        while(ai.hasNext()){
            System.out.println(ai.next());
        }
				
        
        HashSet<String> hs = new HashSet<String>();
        hs.add("one");
        hs.add("two");
        hs.add("two");
        hs.add("three");
        hs.add("three");
        hs.add("five");
        Iterator<String> hi = hs.iterator();
        System.out.println("\nhashset");
        while(hi.hasNext()){
            System.out.println(hi.next());
        }
        
        System.out.println("\n\n\n");
        HashSet<Integer> A = new HashSet<Integer>();
        A.add(1);
        A.add(2);
        A.add(3);
         
        HashSet<Integer> B = new HashSet<Integer>();
//        B.add(3);
        B.add(4);
        B.add(5);
         
        HashSet<Integer> C = new HashSet<Integer>();
        C.add(1);
        C.add(2);
        
        
        System.out.println(A.containsAll(B)); // false
        System.out.println(A.containsAll(C)); // true
        
        
	}

}
