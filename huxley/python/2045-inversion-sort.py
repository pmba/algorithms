
def inversion(array):
    inv = 0
    
    if len(array) > 1:
        pivot = len(array)//2
        left = array[:pivot]
        right = array[pivot:]

        inv = inversion(left)
        inv += inversion(right)

        i = j = k = 0
        left.append(float('Inf'))
        right.append(float('Inf'))
        
        while i < len(left) and j < len(right) and k < len(array):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
                inv += pivot - i
            k += 1
    return inv

cases = int(input())
global inv
inv = 0

for i in range(cases):
    inv = 0
    input()
    arr_size = int(input())
    array = [0]*arr_size
    for j in range(arr_size):
        array[j] = int(input())
    print(inversion(array))
