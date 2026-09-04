class Node:
    def __init__(self, valor):
        self.valor = valor      # Armazena o dado
        self.proximo = None     # Aponta para o próximo nó (inicialmente vazio)

class LinkedList:
    def __init__(self):
        self.head = None  # Lista vazia no início

    # Método para inserir um elemento no final da lista
    def append(self, valor):
        novo_no = Node(valor)
        
        # Se a lista estiver vazia, o novo nó vira a cabeça
        if self.head is None:
            self.head = novo_no
            return

        # Caso contrário, percorre até o último nó
        atual = self.head
        while atual.proximo is not None:
            atual = atual.proximo
        
        # Define o próximo do último nó como o novo nó
        atual.proximo = novo_no

    # Método para exibir os elementos da lista
    def mostrar(self):
        atual = self.head
        elementos = []
        while atual is not None:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        print(" -> ".join(elementos))


# Criando a lista encadeada
lista = LinkedList()

# Adicionando valores
lista.append(10)
lista.append(20)
lista.append(30)

# Mostrando os elementos: 10 -> 20 -> 30
lista.mostrar()
