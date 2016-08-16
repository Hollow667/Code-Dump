public class BinarySearch {

    public int binarySearch(int[] inputArr, int key) {
        int start = 0;
        int end = inputArr.length - 1;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (key == inputArr[mid]) {
                return mid;
            } if (key < inputArr[mid]) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {

        BinarySearch binary = new BinarySearch();
        
        int[] arr = { 2,4,6,8,10,12,14,16 };
        System.out.println("Pozitia elementului 14 : " + binary.binarySearch(arr, 14));
        int[] arr1 = { 6,34,78,123,432,9000 };
        System.out.println("Pozitia elementului 432 : " + binary.binarySearch(arr1, 432));
    }
}
