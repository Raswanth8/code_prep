from heapq import heappush,heappop

def heap_sort(a):
    heap = []
    for element in a:
        heappush(heap,element)
    
    sorted = []

    while heap:
        sorted.append(heappop(heap))

    return sorted

a = [1,23,5,11]
print(heap_sort(a))
