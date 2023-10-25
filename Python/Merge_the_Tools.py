def merge_the_tools(string, k):
    lista = []
    inicio = 0
    fim = k
    while True:
        if len(string)< fim:
            fim = len(k)
        for i in range(inicio, fim):
            if string[i]not in lista:
                lista.append(string[i])
        lista = "".join(lista)
        print(lista)
        lista = []
        if fim == len(string):
            break
        inicio += k
        fim += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)