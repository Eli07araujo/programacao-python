nome = "eLIsEU"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "     Olá mundo!   "


print(texto + ".")
print(texto.strip()+ ".")
print(texto.rstrip()+ ".")
print(texto.lstrip()+ ".")

menu = "python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))

# strings parte 2, com %, f e format

nome = "Eliseu"
idade   = 34
profissão = "Progamador"
Linguagem = "Python"
saldo = 45.435

dados = {"nome": "Eliseu", "idade": 34}

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {nome} Idade: {age} {nome} {nome} {age}".format(age=idade, nome=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")


# FATIAMENTO DE STRING

nome = "Eliseu Mota De Araujo"

print(nome[0])

print(nome[:7])

print(nome[7:])

# STRINGS MÚLTIPLAS LINHAS

nome = "Eliseu"

mensagem = f"""
    Olá meu nome é {nome},
eu estou aprendendo python.
    essa mensagem tem diferentes recuos. 
"""

print(mensagem)

print("""
      ########### MENU ##########
      
      1 - Depositar
      2- Sacar
      0 - sair
      
      ===============================
      
            Obrigado por usar nosso sistema!
      """
      )


PI = 3.14159                                                     
print(f"Valor de PI: {PI:.2f}")  

texto = "  Python  ".lstrip()
print(texto)