# 1. Classe Livro
# Vamos começar definindo a classe Livro, que representa um livro específico.
class Livro: 
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
# 2. Classe Biblioteca
# A classe Biblioteca gerencia uma coleção de objetos Livro.
class Biblioteca:    
    def __init__(self, lista=None):
        self.livros = lista if lista is not None else []
        
    def add(self, livro):
        self.livros.append(livro)

    def catalogo_livro(self):
        for i, el in enumerate(self.livros):
            print(f"{i} - livro: {el.titulo} - {el.autor}")

# Explicação do Código
# __init__: Inicializa a biblioteca com uma lista de livros. Se a lista não for fornecida, inicia como vazia.
# Métodos:
# add: Adiciona um novo livro à lista de livros.
# catalogo_livro: Exibe todos os livros na biblioteca.

biblioteca_x = Biblioteca()
livro1 = Livro("Dom Casmurro", "Machado de Assis")
biblioteca_x.add(livro1)

livro2 = Livro("Pedra Filosofal", "J.K. Rowling")
biblioteca_x.add(livro2)

biblioteca_x.catalogo_livro()
# Saída:
# 0 - livro: Dom Casmurro - Machado de Assis
# 1 - livro: Pedra Filosofal - J.K. Rowling

# Diagrama UML das Classes Livro e Biblioteca
# Aqui está a representação em diagrama UML das classes Livro e Biblioteca:
# ┌────────────────────────────┐
# │         Livro             │
# ├────────────────────────────┤
# │ - titulo: str             │  ← Atributo que representa o título do livro
# │ - autor: str              │  ← Atributo que representa o autor do livro
# ├────────────────────────────┤
# │ + __init__(titulo, autor)  │  ← Construtor que inicializa os atributos titulo e autor
# └────────────────────────────┘

#                     ▲
#                     │  (Usa)
#                     │
# ┌────────────────────────────┐
# │        Biblioteca          │
# ├────────────────────────────┤
# │ - livros: List[Livro]      │  ← Atributo que armazena uma lista de objetos Livro
# ├────────────────────────────┤
# │ + __init__(lista=None)     │  ← Construtor que inicializa a lista de livros
# │ + add(livro: Livro)        │  ← Método que adiciona um livro à lista
# │ + catalogo_livro()         │  ← Método que exibe o catálogo de livros na biblioteca
# └────────────────────────────┘