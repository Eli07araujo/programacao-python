print(1 + 10)
print(1.5 + 5 + 1.5)
print(True)

print(False)
print("Python")


nome = "Zeus"
idade = 34

nome, idade = "Eliseu", 27

print(nome, idade)

limite_saque_diario = 1000

BRAZILIAN_STATES = ["SP", "RJ",]

print(BRAZILIAN_STATES)

CONVERTENDO_TIPOS = []

print(int(1.52456841))
print(int("10"))
print(float("10.10"))
print(float(100))

print(str(10.10))
  


nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(nome, idade)
print(nome, idade, end=" ... \n")
print(nome, idade, sep="#", end=" ... \n")
print(nome, idade, sep="#")



valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))

print(100 / 2)
print(100 // 2)

TIPOS_DE_OPERADORES_ARITMETICOS = []

produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = (10 + 5) * 4
y = (10 / 2) * 25 *((2 - 2) ** 2)
print(x)
print(y)

OPERADORES_DE_COMPARACAO = []

saldo = 200
saque = 200

print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)
print(saldo < saque)
print(saldo <= saque)

OPERADORES_DE_ATRIBUICAO = []

saldo = 500
print(saldo)

saldo = 200
print(saldo)

saldo += 5
print(saldo)

saldo += 10
print(saldo)

saldo -= 5
print(saldo)

saldo //= 2
print(saldo)

saldo /= 2
print(saldo)

saldo *= 10
print(saldo)

saldo %= 4
print(saldo)

# AND = para ser true tudo tem que ser true
# OR = para ser true apenas um tem que ser true

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = ( saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

# OPERADORES DE IDENTIDADE

saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)

# OPERADORES DE ASSOCIAÇAO

frutas = ["limão","uva"]

print("laranja" in frutas)
print("limão" in frutas)

# identação de blocos

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire seu dinheiro na boca do caixa!")

    print("obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo  += valor


sacar(1000)



# Estruturas condicionais

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade:"))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")   
else:
    print("Ainda nao pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")   
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
      print("Ainda nao pode tirar a CNH.")






 