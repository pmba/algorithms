global array
array = [2, 3, 46, 7, 5]

def insertionSort(arr):
    for j in range(2, len(arr)):
        key = arr[j]
        i = j - 1
        while i > 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i+1] = key

insertionSort(array)
print(array)

"""

Estudo do custo:


    def insertionSort(arr):
    
    for j in range(2, len(arr)): - EXECUTA N VEZES, POIS TEM A ULTIMA
                                   VERIFICAÇÃO PARA A SAIDA DO LOOP
                                   (CONSTANTE C1)
    
        key = arr[j] - EXECUTA N-1 VEZES (CONSTANTE C2)
        i = j - 1    - EXECUTA N-1 VEZES (CONSTANTE C3)
        
        while i > 0 and arr[i] > key: - SOMATÓRIO j=2 ATÉ N DE T(j)
                                        (CONSTANTE C4)

            arr[i + 1] = arr[i] - SOMATÓRIO j=2 ATÉ N DE T(j)-1
                                  (CONSTANTE C5)
            i -= 1              - SOMATÓRIO j=2 ATÉ N DE T(j)-1
                                  (CONSTANTE C6)
            
        arr[i+1] = key - EXECUTA N-1 VEZES (CONSTANTE C7)

Equação do Insertion Sort (Soma de todos os custos de cada linha):

    T(n) = C1*N + C2*(N-1) + C3*(N-1) + C4*(SOMATÓRIO j=2 ATÉ N DE T(j)) +
           C5*(SOMATÓRIO j=2 ATÉ N DE T(j)-1) + C6*(SOMATÓRIO j=2 ATÉ N DE T(j)-1) +
           C7*(N-1)

Melhor caso:

    Array já ordenado
    [1, 2, 3, 7, 9, 11, 13]
    => Não entra no caso da constante C5 e C6
    => O caso da constante C4 vira SOMATÓRIO j=2 ATÉ N DE 1, i.e, (N-1)

    T(n) = C1*N + C2*(N-1) + C3*(N-1) + C4*(N-1) + C7*(N-1)
         = C1*N + C2*N - C2 + C3*N - C3 + C4*N - C4 + C7*N - C7
         = N*(C1 + C2+ C3+ C4 + C7) + (- C2 - C3 - C4)
         
    T(n) = A*N + B

Pior Caso:

    Array na ordem inversa
    [10, 7, 6, 5, 2, 1]
    => T(j) = j

    SOMATÓRIO j=2 ATÉ N DE T(j)   = 2 + 3 + 4 + 5 + ... + N     = (N*(N+1))/2 - 1
    SOMATÓRIO j=2 ATÉ N DE T(j)-1 = 2 + 3 + 4 + 5 + ... + (N-1) = ((N-1)*(N-1+1))/2 = (N*(N-1))/2

    T(n) = ...
    T(n) = A*N^2 + B*N + C


"""
