def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f'Mova o Disco 1 de {origem} para {destino}')
        return 1
    movimentos = 0
    movimentos += hanoi(n - 1, origem, auxiliar, destino)
    print(f'Mova o disco {n} de {origem} para {destino}')
    movimentos += 1
    movimentos += hanoi(n - 1, auxiliar, destino, origem)
    return movimentos


num_discos = 10
total_mov = hanoi(num_discos,'A','C','B')
print(f'Total de movimentos necessários: {total_mov}')


#torre de hanoi usando recursividade
