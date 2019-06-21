#program to count the number of inversions piggybacking on merge sort
def Merge_CountSplitinv(left,right):
        result=[]
        i,j=0,0
        count = 0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                b = left[i:]
                count += len(b
                j+=1
        result += left[i:]
        result += right[j:]

        return  (result, count)

#sort_count function
def sort_count(A):
    #base case : return list if length <= 1
    n = len(A)
    if  n <= 1:
        return (A, 0)

    # B and C are the sorted version of the first and second partsof the array A respectively while D is the sorted version of A
    #recursively sort the left(B) and right(C) of A
    B,X = sort_count(A[:(n//2)])
    C,Y = sort_count(A[(n//2):])
    D,Z = Merge_CountSplitinv(B,C)

    return  (D, X+Y+Z)

def main():
    #open file, create a list a list of numbers and call the sort_count function on the list
    with open('inversion.txt', 'r') as f:
        print(sort_count([int(l) for l in f]))





main()
