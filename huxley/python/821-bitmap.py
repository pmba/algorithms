def divideMatrix(matrix, inirow, inicol, endrow, endcol):
    if (inirow == endrow) and (inicol == endcol):
        return matrix[inirow][inicol]
    elif (inirow < endrow) and (inicol < endcol):
        midrow = (endrow+inirow)//2
        midcol = (endcol+inicol)//2

        quad1 = divideMatrix(matrix, inirow, inicol, midrow, midcol)
        quad2 = divideMatrix(matrix, inirow, midcol+1, midrow, endcol)
        quad3 = divideMatrix(matrix, midrow+1, inicol, endrow, midcol)
        quad4 = divideMatrix(matrix, midrow+1, midcol+1, endrow, endcol)

        if quad1 and quad2 and quad3 and quad4:
            print(quad1)
            return quad1
        else:
            print('D')
            print('%d%d%d%d' % (quad1, quad2, quad3, quad4))
            return quad1
            
    elif (inirow < endrow) and (inicol == endcol):
        midrow = (endrow+inirow)//2

        quad1 = divideMatrix(matrix, inirow, inicol, midrow, endcol)
        quad2 = divideMatrix(matrix, midrow+1, inicol, endrow, endcol)

        if quad1 == quad2:
            print(quad1)
        else:
            print('D%d%d' % (quad1, quad2))
    elif (inirow == endrow) and (inicol < endcol):
        midcol = (endcol+inicol)//2

        quad1 = divideMatrix(matrix, inirow, inicol, endrow, midcol)
        quad2 = divideMatrix(matrix, inirow, midcol+1, endrow, endcol)

        if quad1 == quad2:
            print(quad1)
        else:
            print('D%d%d' % (quad1, quad2))

cases = int(input())
while cases:
    row, col = [int(x) for x in input().split()]
    matrix = []
    for i in range(row):
        matrix.append([int(x) for x in input()])
    maxrow = len(matrix)-1
    maxcol = len(matrix[0])-1
    print(maxrow, maxcol)
    divideMatrix(matrix, 0, 0, maxrow, maxcol)
    cases -= 1
        
