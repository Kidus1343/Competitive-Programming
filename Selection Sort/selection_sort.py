# User function Template for python3

class Solution:
    def select(self, arr, i):
        # code here
        min_index = i
        for j in range(i + 1, len(arr)):
            if (arr[j] < arr[min_index]):
                min_index = j
        return min_index

    def selectionSort(self, arr, n):
        # code here
        for j in range(n):
            min_index = self.select(arr, j)
            if min != j:
                temp = arr[min_index]
                arr[min_index] = arr[j]
                arr[j] = temp
