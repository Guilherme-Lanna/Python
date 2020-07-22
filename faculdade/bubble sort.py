##Bubble Sort

##procedure bubbleSort( A : lista de itens ordenaveis ) defined as:
##  do
##    trocado := false
##    for each i in 0 to length( A ) - 2 do:
##      // verificar se os elementos estão na ordem certa
##      if A[ i ] > A[ i + 1 ] then
##        // trocar elementos de lugar
##        trocar( A[ i ], A[ i + 1 ] )
##        trocado := true
##      end if
##    end for
##  // enquanto houver elementos sendo reordenados.
##  while trocado
##end procedure

def bubbleSort(A):
    trocado = True
    cont = 1
    while trocado:
        trocado = False
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                temp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp
                trocado = True
                print(cont, ":", A)
                cont = cont + 1


lista = [13, 3, 25, 7, 8, 10, 1, 50, 9, 11, 43, 6]

print("Lista Desordenada")
print(lista)
print("")

bubbleSort(lista)
print("Lista Ordenada")
print(lista)