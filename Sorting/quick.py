"""
It is alse based on Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.

"""
def quick_sort(a):
    elements = len(a)

    if elements < 2 :
        return a
    
    current_p = 0
    for i in range(1,elements):
        if a[i] <= a[0]:
            current_p +=1
            temp = a[i]
            a[i] = a[current_p]
            a[current_p] = temp
    
    temp = a[0]
    a[0] = a[current_p]
    a[current_p] = temp

    left = quick_sort(a[0:current_p])
    right = quick_sort(a[current_p+1:elements])

    a = left +[a[current_p]]+right

    return a

a = [1,23,5,11]
print(quick_sort(a))
