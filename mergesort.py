def mergesort(L):
    if len(L) == 1:
        return L
    
    print L, len(L)   

    if len(L) > 1 :
        mid = len(L)//2
        left = L[:mid]
        right = L[mid:]
        L_sorted = L

        left = mergesort(left)
        right = mergesort(right)

        print 'split', L, len(L), 'L,R', left, right

        i = j = k = 0
        while j < len(left) and k < len(right):
            if left[j] < right[k]:
                L_sorted[i] = left[j]    
                j += 1 
            else:
                L_sorted[i] = right[k]
                k += 1
            i += 1 

        while j < len(left):
            L_sorted[i] = left[j]
            j += 1 
            i += 1
        while k < len(right):
            L_sorted[i] = right[k]
            k += 1 
            i += 1 
        
        print L_sorted
        return L_sorted

            
                


