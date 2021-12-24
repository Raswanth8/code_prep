"""
It is based on Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves

"""
def merge_sort(a):
    if len(a) > 1 :
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        # Recursive call
        merge_sort(left)
        merge_sort(right)

        # Two iterators for left and right
        i = 0
        j = 0
        # Iterator for main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]: # Left slot
                a[k] = left[i]
                i+=1
            else:
                a[k] = right[j] # Right slot
                j+=1
            k+=1 # Move to the next slot
        # For remaining elements
        while i < len(left):
            a[k] = left[i]
            i+=1
            k+=1
        
        while j < len(right):
            a[k] = right[j]
            j+=1
            k+=1
    

a = [1,23,5,11]
merge_sort(a)
for e in range(len(a)):
        print(a[e])




