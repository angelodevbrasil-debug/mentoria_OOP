# Antes de entrar nas classes, vamos rever como calcular a área e o 
# perímetro de um retângulo usando funções.

def area_retagulo(base, altura):
    return base * altura

def perimetro_retangulo(base, altura):
    return 2 * (base + altura)

print(area_retagulo(5, 10))  # Saída: 50
print(perimetro_retangulo(5, 10))  # Saída: 30

# area_retagulo: Esta função calcula e retorna a área do retângulo.
# perimetro_retangulo: Esta função calcula e retorna o perímetro do retângulo.

#Encapsulando Comportamentos na Classe Retangulo
class Retangulo:
    
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
# Explicação do Código
# Retangulo: Classe que representa um retângulo.
# Atributos: base e altura são usados para armazenar medidas do retângulo.
# Métodos:
# area: Retorna a área do retângulo.
# perimetro: Retorna o perímetro do retângulo.

retg1 = Retangulo(50, 10)
print(retg1.area())     # Saída: 500
print(retg1.perimetro())  # Saída: 120

retg2 = Retangulo(5, 3)
print(retg2.area())     # Saída: 15
print(retg2.perimetro())  # Saída: 16

# Diagrama UML da Classe Retangulo
# Aqui está a representação da classe Retangulo em um diagrama UML:
# ┌───────────────┐
# │   Retangulo   │
# ├───────────────┤
# │ - base : int  │
# │ - altura : int│
# ├───────────────┤
# │ + area()      │
# │ + perimetro() │
# └───────────────┘