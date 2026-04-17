# ### **1- Classe Pessoa**

# Crie uma classe `Pessoa` com os atributos `nome` e `idade`. 
# Adicione um método `apresentar()` 
# que exiba `"Olá, meu nome é [nome] e tenho [idade] anos."` 
# Crie duas pessoas diferentes e chame o método.

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade


#     def exibir(self):
#         print(f"Olá meu nome é {self.nome} e tenho {self.idade}")
    
# nome1 = Pessoa("José", 42)
# nome1.exibir()
# nome2 = Pessoa("Maria", 22)
# nome2.exibir()

# ---

### **2.Classe Retângulo**

# Crie uma classe `Retangulo` com os atributos `largura` e `altura`. Adicione métodos:

# - `calcular_area()` – retorna a área
# - `calcular_perimetro()` – retorna o perímetro
    
#     Crie um retângulo com largura 5 e altura 3 e exiba sua área e perímetro.

# class Retangulo:
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura

#     def calcular_area(self):
#         return self.largura * self.altura    

#     def calcular_perimetro(self):
#         return (self.largura + self.altura)
    
# ret = Retangulo(5, 3)
# print("Área", ret.calcular_area())
# print("Perimetro", ret.calcular_perimetro())


# ---

# ### **3.   Classe Conta Bancária**

# Crie uma classe `ContaBancaria` com:

# - Atributos: `titular`, `saldo` (inicial 0)
# - Métodos:
#     - `depositar(valor)`: acrescenta ao saldo
#     - `sacar(valor)`: se houver saldo suficiente, subtrai; senão, exibe `"Saldo insuficiente"`
#     - `exibir_saldo()`: mostra o saldo formatado
        
#         Crie uma conta, faça depósitos e saques e exiba o saldo.

class Conta_bancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
       
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if valor <= self.saldo:
             self.saldo = self.saldo - valor
             print(f"Saque de R$ {valor:.2f} realizado com sucesso")
        else:
            print("Saldo Insuficiente")    
            
    def exibir_saldo(self):        
        print(f" Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")  
    


conta = Conta_bancaria("Jose")

conta.exibir_saldo()
conta.depositar(1000)
conta.depositar(500)
conta.sacar(200)
conta.sacar(2000)
conta.exibir_saldo()
conta.sacar(1300)
conta.exibir_saldo()
conta.depositar(5000)
conta.exibir_saldo()

''








# ---

# ### **4. Classe Produto**

# Crie uma classe `Produto` com:

# - Atributos: `nome`, `preco`, `quantidade_estoque`
# - Métodos:
#     - `total_estoque()`: retorna `preco * quantidade_estoque`
#     - `adicionar_estoque(quantidade)`: aumenta a quantidade
#     - `remover_estoque(quantidade)`: diminui, mas não permite ficar negativo
        
#         Crie um produto, altere o estoque e exiba o valor total.

class Produto:

    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def total_estoque(self):
        return self.preco * self.quantidade_estoque
    
    def adicionar_estoque(self, quantidade):
        self.quantidade_estoque = self.quantidade_estoque + self.adicionar_estoque
        print(f"{quantidade} unidade(s) adicionada(s). Estoque atual:
              


    def remover_estoque(self):
        self.remover_estoque = True
        return 
    

produto1 = Produto("Pao")











# # ---

# # ### **5. Classe Aluno**

# # Crie uma classe `Aluno` com:

# # - Atributos: `nome`, `matricula`, `notas` (lista de floats)
# # - Métodos:
# #     - `adicionar_nota(nota)`: adiciona à lista
# #     - `calcular_media()`: retorna a média das notas
# #     - `situacao()`: retorna `"Aprovado"` se média >= 7, `"Recuperação"` se >= 5, `"Reprovado"` caso contrário
        
# #         Crie um aluno, adicione 3 notas e exiba sua situação.


# class Aluno:
#     def __init__(self, nome, matricula, notas):
#         self.nome = nome
#         self.matricula = matricula
#         self.notas = notas

#     def nota(self):
#         self.nota = []

#     def media(self):
#         self.calcular_media()
#         return self.calcular_media
    
#     def situacao (self):
#         return "aprovado" if self.media >=7 and "recuperacao" if self.media <=5  else


