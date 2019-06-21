#Quicksort using the first element of the array as the pivot(P)
#partition subroutine - partions array(A) around a pivot(P) element
def partition(A, l, r ):
    p = A[l]
    i = l+1
    k = l+1
    for j in range(k,r+1):
        if A[j] < p:
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
            i = i+1
        else:
            pass
    t = A[l]
    A[l] = A[i-1]
    A[i-1] = t

    return i-1

def quicksort(array):
    c = quicksort_helper(array,0,len(a)-1)
    return array

def quicksort_helper(array,first,last):
    if first < last:
        pivot = partition(array, first, last)
        quicksort_helper(array,first, pivot-1)
        quicksort_helper(array, pivot+1, last)


def main():
    #sorts by calling quicksort on a created list of numbers in from a txt file
    with open('Quicksort.txt', 'r') as f:
        print(quicksort([int(l) for l in f]))
main()
