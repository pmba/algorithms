def buscaBinaria(arr, ini, fim, num):
    if ini <= fim:
        mid = (ini+fim)//2
        #print('Inicio: %d' % ini)
        #print('Final: %d' % fim)
        #print('Pivô: %d' % mid)

        if num == arr[mid]:
            return mid
        elif num > arr[mid]:
            return buscaBinaria(arr, mid+1, fim, num)
        else:
            return buscaBinaria(arr, ini, mid-1, num)
    else:
        return -1

caso = 1

while True:
    qmar, qcon = list(map(int, input().split()))

    if qmar == 0 and qcon == 0:
        break

    print('CASE# %d:' % caso)
    caso += 1

    arr = []
    for i in range(qmar):
        arr.append(int(input()))

    arr.sort()

    for i in range(qcon):
        num = int(input())
        res = buscaBinaria(arr, 0, len(arr)-1, num)

        if res == -1:
            print('%d not found' % num)
        else:
            print('%d found at %d' % (num, res+1))
    
