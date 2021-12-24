"""
It sorts an array by repeatedly finding the minimum element (considering decresing order) from unsorted part and putting it at the beginning.

"""

def selection_sort(a):
    for i in range(len(a)): # Traverse through entire array
        min_index = i
        j = i
        for j in range(i+1,len(a)): # Find min in remaining unsorted array
            if a[j] < a[min_index]:
                min_index = j
            
        a[i],a[min_index] = a[min_index],a[i] # swap min

    for i in range(len(a)):
        print(a[i])

selection_sort([1,3,2,4])
