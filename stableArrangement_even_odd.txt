import java.util.*;
public class stable{
	public static void main(String args[]){
		List<Integer> list = new ArrayList<>();
		list.add(5);	list.add(7);
		list.add(15);	list.add(20);
		list.add(22);	list.add(24);
		list.add(27);	list.add(25);
		list.add(75);
		int j=0,x;
		for (int i=0;i<list.size();i++){
			x=list.get(i);
			if(x%2==0){
				list.remove(i);
				list.add(j,x);
				j++;
			}
		}
	system.out.println(list);
	}
}

