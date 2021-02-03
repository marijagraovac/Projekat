def bubble_sort(lista, kljuc):
    n = len(lista)
    for j in range(n):
        for i in range(n-1-j):
            if lista[i][kljuc] > lista[i+1][kljuc]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp