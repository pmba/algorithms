def firstK(arr):
    k = 0
    #first rung
    k = max(k, arr[0])
    #other rungs
    for i in range(1, len(arr)):
        k = max(k, arr[i] - arr[i-1])
    return k

def tryK(arr, k):
    dis = arr[0]
    if dis > k:
        return False
    if dis == k:
        k -= 1

    for i in range(1, len(arr)):
        dis = arr[i] - arr[i-1]
        if dis > k:
            return False
        if dis == k:
            k -= 1
    return True

def findK(arr, lo, hi, best):
    if lo <= hi:
        mid = (lo+hi)//2

        if tryK(arr, mid):
            return findK(arr, lo, mid-1, mid)
        else:
            return findK(arr, mid+1, hi, best)
    else:
        return best

arr = [int(x) for x in input().split()]
print(findK(arr, 0, sum(arr), firstK(arr)))