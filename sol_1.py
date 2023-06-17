# ans 1
def sqrt(x):
    if x == 0 or x == 1:
        return x

    left = 1
    right = x // 2

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square > x:
            right = mid - 1
        else:
            left = mid + 1

    return right

print(sqrt(4)) 
print(sqrt(8))  

