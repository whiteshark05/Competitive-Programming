#### Template
### First True [FFFFFFTTTTTTT]
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    lo, hi = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while lo != hi:
        mid = (lo + hi) >> 1
        if condition(mid):
            hi = mid #Moving left
        else:
            lo = mid + 1 #Moving right
    return lo

### Last True [TTTTTTTFFFFFFF]
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    lo, hi = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while lo != hi:
        mid = (lo + hi + 1) >> 1
        if condition(mid):
            lo = mid #Moving right
        else:
            hi = mid - 1 #Moving left
    return lo


#### Practice
import bisect
A = [1,1,2,3,4,8,9,9,9,9,10]

#Lowerbound/BisectLeft: First true when array[mid] <= target
def bs_left(array, target) -> int:
    def condition(mid) -> bool:
    	return target <= array[mid]
        #pass

    lo, hi = 0, len(array)  # Search space can be N when target exceeds the array max value
    while lo != hi:
        mid = (lo + hi) >> 1
        if condition(mid):
            hi = mid #Moving left
        else:
            lo = mid + 1 #Moving right
    return lo 

#Upperbound/BisectRight: First true when 
def bs_right(array, target) -> int:
    def condition(mid) -> bool:
        return target < array[mid]

    lo, hi = 0, len(array)  # could be [0, n], [1, n] etc. Depends on problem
    while lo != hi:
        mid = (lo + hi) >> 1
        if condition(mid):
            hi = mid #Moving left
        else:
            lo = mid + 1 #Moving right
    return lo 

for target in range(-10, 20):
	print(target, bisect.bisect_left(A, target), bs_left(A, target))
	print(target, bisect.bisect_right(A, target), bs_right(A, target))