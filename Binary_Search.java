
//metoda de cautare binara

public class Binary_Search {
	//metoda de cautare 
	//primul parametru reprezinta array-ul in care cautam
	//cel de-al doilea este elementul cautat
	public static int binarySearch(String[] theData, String wanted)
	{
	    //-1 inseamna ca elementul nu a fost gasit
	    int foundIndex=-1;
	 
	    //retine capetele intervalului de cautare
	    int top = theData.length-1;
	    int bottom = 0;
	 
	    //parcurge array-ul, divizand intervalul de cautare
	    while(bottom<=top)
	    {
	        //calculeaza mijlocul sectiunii analizate
	        int middle = (top+bottom)/2;
	 
	        //compara elementul din mijloc cu elementul cautat 
	        int comp = theData[middle].compareTo(wanted);
	 
	        //daca elementul din mijloc este egal cu elementul cautat, returneaza indexul sau
	        if(comp==0)
	            return middle;
	 
	        /* daca elementul din mijloc este mai mare, 
	         * atunci elementul cautat se afla in prima jumatate
	         * altfel se afla in cea de-a doua jumatate
	         */
	 
	        else if(comp>0) //mijlocul este mai mare
	            top=middle-1;
	        else //mijlocul este mai mic
	            bottom=middle+1;
	 
	    }
	 
	    //am terminat cautarea
	    return foundIndex;
	}
}


/*Call with v in main
 
 array ordonat

String[] sortedStrings = {"aubergine", "carrot", "courgette",
"leek", "onion", "potato", "turnip"};

//apeleaza metoda de cautare - returneaza -1 daca elementul nu este gasit
int searchResult = binarySearch(sortedStrings, "potato");

System.out.println("gasit la indexul: "+searchResult);
*/
