"""
It works by repeatedly swapping the adjacent wrong elements.

"""
def bubble_sort(a):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)-1):
            if (a[j]>a[j+1]):
                a[j],a[j+1] =a[j+1],a[j]

    for i in range(len(a)):
        print(a[i])

bubble_sort([1,3,2,5])