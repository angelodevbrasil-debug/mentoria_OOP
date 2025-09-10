# Programação Orientada a Objetos (OOP) em Python

Este repositório contém exemplos práticos de conceitos fundamentais de Programação Orientada a Objetos em Python, organizados de forma didática para facilitar o aprendizado.

## 📁 Estrutura do Projeto

```
├── 01-introducao.py     # Conceitos básicos de OOP
├── 02-cachorro.py       # Primeira classe prática
├── 03-rentagulo.py      # Encapsulamento e métodos
├── 04-biblioteca.py     # Composição e relacionamento entre classes
└── README.MD            # Este arquivo
```

## 📚 Conteúdo dos Arquivos

### [01-introducao.py](01-introducao.py)
Introdução aos conceitos fundamentais de OOP:
- Definição de classes e objetos
- Conceitos de atributos e métodos
- Base teórica para os exemplos práticos

### [02-cachorro.py](02-cachorro.py)
Implementação da classe [`Cachorro`](02-cachorro.py) demonstrando:
- Construtor `__init__`
- Atributos de instância (nome, idade, raça, cor)
- Métodos de comportamento ([`latir()`](02-cachorro.py), [`comer()`](02-cachorro.py))
- Instanciação e manipulação de objetos

**Diagrama UML:**
```
┌───────────────┐
│  Cachorro     │
├───────────────┤
│ - nome : str  │ 
│ - idade : int │  
│ - raca : str  │
│ - cor : str   │ 
├───────────────┤
│ + latir()     │
│ + comer()     │
└───────────────┘
```

### [03-rentagulo.py](03-rentagulo.py)
Comparação entre programação procedural e orientada a objetos:
- Funções para cálculo de área e perímetro
- Classe [`Retangulo`](03-rentagulo.py) com métodos encapsulados
- Demonstração de encapsulamento de comportamentos

**Diagrama UML:**
```
┌───────────────┐
│   Retangulo   │
├───────────────┤
│ - base : int  │
│ - altura : int│
├───────────────┤
│ + area()      │
│ + perimetro() │
└───────────────┘
```

### [04-biblioteca.py](04-biblioteca.py)
Sistema de biblioteca demonstrando:
- Classe [`Livro`](04-biblioteca.py) com atributos básicos
- Classe [`Biblioteca`](04-biblioteca.py) gerenciando coleção de livros
- Composição e relacionamento entre classes
- Métodos de manipulação de coleções

**Diagrama UML:**
```
┌────────────────────────────┐
│         Livro             │
├────────────────────────────┤
│ - titulo: str             │
│ - autor: str              │
├────────────────────────────┤
│ + __init__(titulo, autor)  │
└────────────────────────────┘
                ▲
                │ (Usa)
                │
┌────────────────────────────┐
│        Biblioteca          │
├────────────────────────────┤
│ - livros: List[Livro]      │
├────────────────────────────┤
│ + __init__(lista=None)     │
│ + add(livro: Livro)        │
│ + catalogo_livro()         │
└────────────────────────────┘
```

## 🚀 Como Executar

Para executar qualquer um dos exemplos, use o Python 3:

```bash
python 01-introducao.py
python 02-cachorro.py
python 03-rentagulo.py
python 04-biblioteca.py
```

## 💡 Conceitos Abordados

- **Classes e Objetos**: Definição e instanciação
- **Atributos**: Características dos objetos
- **Métodos**: Comportamentos e funcionalidades
- **Construtor**: Inicialização de objetos com `__init__`
- **Encapsulamento**: Agrupamento de dados e comportamentos
- **Composição**: Relacionamento entre classes

## 📖 Ordem de Estudo Recomendada

1. Comece com [01-introducao.py](01-introducao.py) para entender os conceitos básicos
2. Pratique com [02-cachorro.py](02-cachorro.py) para ver uma classe simples em ação
3. Compare abordagens em [03-rentagulo.py](03-rentagulo.py) (procedural vs OOP)
4. Explore relacionamentos entre classes em [04-biblioteca.py](04-biblioteca.py)

## 🎯 Objetivos de Aprendizado

Ao final deste estudo, você será capaz de:
- Criar classes e objetos em Python
- Implementar construtores e métodos
- Entender a diferença entre programação procedural e orientada a objetos
- Trabalhar com composição e relacionamentos entre classes
- Aplicar conceitos de encapsulamento

---

*Este material foi desenvolvido para ensino de Programação Orientada a Objetos em Python.*