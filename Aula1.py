entra = []

# 1. Leitura dos números
while True:
    num = float(input("Digite um número (-1 para sair): "))
    if num == -1:
        break                  # Sai do loop quando o usuário digita -1
    entra.append(num)          # Adiciona o número lido à lista 'entra'

# 2. Ordenação da lista com Selection Sort
n = len(entra)                # Guarda o tamanho da lista

for i in range(n):
    menor_indice = i           # Assume que o elemento atual é o menor
    
    # Varre os elementos restantes para encontrar um valor menor
    for j in range(i + 1, n):
        if entra[j] < entra[menor_indice]:
            menor_indice = j   # Atualiza o índice do menor valor encontrado

    # Troca o elemento atual com o menor encontrado
    entra[i], entra[menor_indice] = entra[menor_indice], entra[i]

# 3. Exibe a lista ordenada
print("Lista ordenada:", entra)
