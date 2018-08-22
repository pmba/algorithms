n,m,o = input().split()

n = int(n)  #Linhas da Matriz A
m = int(m)  #Colunas da Matriz A e Linhas da Matriz B
o = int(o)  #Colunas da Matriz B

#Cria a matriz A
matrixA = [[0 for x in range(m)] for y in range(n)]
#Cria a matriz B
matrixB = [[0 for x in range(o)] for y in range(m)]

for i in range(n):
    line = input().split()
    for j in range(m):
        matrixA[i][j] = int(line[j])

for i in range(m):
    line = input().split()
    for j in range(o):
        matrixB[i][j] = int(line[j])

for i in range(n):
    for k in range(o):
        element = 0
        for j in range(m):
            element += (matrixA[i][j] * matrixB[j][k])
        print(element, end='')

        if k < o-1:
            print(' ', end='')
            
    print('\n', end='')




        
