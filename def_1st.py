# Criar as três listas
nomes_produtos = ["Produto A", "Produto B", "Produto C"]
precos_produtos = [10.0, 20.0, 15.0]
quantidades_produtos = [5, 10, 8]

# Função para imprimir um produto com base na posição
def imprimir_produto(posicao):
    print(f"Nome: {nomes_produtos[posicao]}, Preço: {precos_produtos[posicao]}, Quantidade: {quantidades_produtos[posicao]}")

# Função para retirar um produto com base na posição
def retirar_produto(posicao):
    del nomes_produtos[posicao]
    del precos_produtos[posicao]
    del quantidades_produtos[posicao]

# Exemplo de uso das funções
imprimir_produto(1)  # Imprime o segundo produto
retirar_produto(0)   # Retira o primeiro produto

# Verificar as listas após a retirada
print("Listas após a retirada:")
print("Nomes:", nomes_produtos)
print("Preços:", precos_produtos)
print("Quantidades:", quantidades_produtos)