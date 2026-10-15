// TODO: This solution does not have the correct complexity. 
class Solution {
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    int[] sorted = new int[nums1.length + nums2.length];
    int index1 = 0, index2 = 0, sortedIndex = 0;
    while (index1 < nums1.length && index2 < nums2.length) {
      if (nums1[index1] < nums2[index2]) {
        sorted[sortedIndex] = nums1[index1];
        index1++;
      } else {
        sorted[sortedIndex] = nums2[index2];
        index2++;
      }
      sortedIndex++;
    }

    while (index1 < nums1.length) {
      sorted[sortedIndex] = nums1[index1];
      index1++;
      sortedIndex++;
    }

    while (index2 < nums2.length) {
      sorted[sortedIndex] = nums2[index2];
      index2++;
      sortedIndex++;
    }

    int middle = sorted.length / 2;
    if (sorted.length % 2 == 0) {
      return (sorted[middle - 1] + sorted[middle]) / 2.0;
    } else {
      return (sorted[middle]);
    }
  }
}
