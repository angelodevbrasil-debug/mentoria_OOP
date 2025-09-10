class Cachorro:
    
    def __init__(self, nome, idade, raca, cor):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.cor = cor
    
    def latir(self):
        print(f"{self.nome} diz: Au Au!")
        
    def comer(self):
        print(f"{self.nome} da raça {self.raca} está comendo ração.")
        

# Explicação do Código
# __init__: Este é o método construtor, que inicializa os atributos do objeto.
# Atributos: nome, idade, raca, cor são os atributos que definem as características do cachorro.
# Métodos:
# latir: Método que faz o cachorro "latir".
# comer: Método que descreve a ação de comer do cachorro.

# Instanciação de um objeto
cachorro1 = Cachorro("Caramelo", 8, "Vira-lata", "branca e caramelo")
cachorro1.nome = "Jambo"
cachorro1.latir()  # Saída: Jambo diz: Au Au!
cachorro1.comer()  # Saída: Jambo da raça Vira-lata está comendo ração.

# Instanciação de um outro objeto
cachorro2 = Cachorro("Newton", 2, "labrador", "amarelo")
cachorro2.comer()  # Saída: Newton da raça labrador está comendo ração.

# Diagrama UML da Classe Cachorro
# Aqui está a representação da classe Cachorro em um diagrama UML:
# ┌───────────────┐
# │  Cachorro     │
# ├───────────────┤
# │ - nome : str  │ 
# │ - idade : int │  
# │ - raca : str  │
# │ - cor : str   │ 
# ├───────────────┤
# │ + latir()     │
# │ + comer()     │
# └───────────────┘