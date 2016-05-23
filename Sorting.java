
//Sortare prin selectie

public class Sorting {

	public static void main(String[] args) {
		
		int [] myData = {1,2,3,4,5,8,22,5,7,1,9};
		 
		//parcurge array-ul intr-o bucla for
		for(int pos=0; pos < myData.length-1; pos++)
		{
		        /* gaseste si retine pozitia 
		         * celui mai mic element
		         * incepe de la pos si cauta in restul array-ului
		         * (pos indica inceputul sectiunii nesortate)
		         */
		    int minIndex = pos;
		 
		        // parcurge sectiunea nesortata
		    for(int next=pos+1; next< myData.length; next++)
		    {
		        if(myData[minIndex]>myData[next])
		            minIndex=next;
		    }
		 
		        //inverseaza pozitia elementelor daca este necesar
		    if(minIndex!=pos)
		    {
		            //retine elementul curent indicat de pos
		        int temp = myData[pos];
		            //copiaza cel mai mic element la pozitia pos
		        myData[pos] = myData[minIndex];
		            //copiaza elementul inlocuit la pozitia minIndex
		        myData[minIndex] = temp;
		    }
		 
		        //afiseaza array-ul sortat
		    for(int p : myData)
		    {    System.out.print(p);    }
		    System.out.println();
		}

	}

}
