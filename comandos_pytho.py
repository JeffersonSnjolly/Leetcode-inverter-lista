# for
for i in range(0,2): print(i)

for x in range(1,3):
    for y in range(0,4):
        print(f"{x} x {y} = {x*y}")
    print("*"*10)
    
# while
i = 0
while i <= 5:
    print(i)
    i += 1
    
# match case
i = 3
match i:
    case 1:
        print("É um")
    case 2:
        print("É dois")
    case _:
        print("Nenhum deles!")
        

# random
import random

num_aleatorio = random.randint(0,3)
print(num_aleatorio)

gpu = ["5090","4090","3080-TI","5080-TI"]
tamanho = len(gpu)
sorteio_gpu = random.randint(0,tamanho)
print(f"Placa de video escolhida {gpu[sorteio_gpu]}")


novo_sorteio = random.choice(gpu)
print(f"Placa de video escolhida {novo_sorteio}")

# Função
def conversor_temperatura(num):
    resutado = (num * 1.8)+32
    return resutado
    
op = float(25)
print(f"{op} graus celsius = {conversor_temperatura(op)} fahrenheit")

# txt com os escrevendo
import os
texto = "Estamos treinando sintaxe em python"
with open(os.path.join("texto_generico.txt"), 'w') as arq:
    arq.write(texto)
    
# txt lendo
with open(os.path.join("texto_generico.txt"), 'r') as arq:
    dado = arq.read()
    
print(dado)

#json escrita
import json
dado = {"Nome":"Jeff","Idade":36,"Cor":"Preto"}
with open(os.path.join("json_generico.json"), "w") as arq:
    arq.write(json.dumps(dado))

#json lendo    
with open(os.path.join("json_generico.json"),"r") as arq:
    aluno = arq.read()

print(aluno)


#lambda
lista = lambda x: x.split()
lista(texto)

#list comprehesion
num = [x for x in range(0,7) if x%2==0]
print(num)

#dict comprehesion 
carros = {"Ferrari":"vermelha","Lamborguini":"preto","mustang":"vermelho","Ford GT":"preto"}

escolhidos = {k:v for k,v in carros.items() if v == "preto"}
print(escolhidos)

# map

x = list(map(lambda x: x.upper(), carros))
print(x)

num = [1,2,3,4,5,6,7,8,9,10]
impares = list(map(lambda x : x % 2 != 0, num))
#retorna valores booleanos
print(impares)

num2 = [1,2,3,4,5,6,7,8,9,10]

somando = list(map(lambda x,y: x+y, num,num2))
print(somando)

#reduce
from functools import reduce

soma = reduce(lambda x,y: x+y, num)
print(soma)

valor_max = reduce(lambda a,b: a if a>b else b, num)
print(valor_max)

#filter
impares = list(filter(lambda x : x%2!=0, num))

print(impares)


#listas
frutas = ["banana","maça","pera"]
print(frutas)
frutas02 = []
print(frutas02)
letras = list("PYTHON")
print(letras)
numeros = list(range(10))
print(numeros)
carros02 = ["Ferrari","F8",4200000,2020,2900,"São Paulo", True]
print(carros02)


# matriz
matriz = [[1,"a",2],
          ["b",3,4],
          [6,5,"c"]]

print(matriz[0])
print(matriz[0][1])
print(matriz[2][2])
print(matriz[-1][-1])

#acessando via for
for k in matriz:
    for v in k:
        print(v)

#Slice
print(letras[2:])
print(letras[:2])
print(letras[::-1])


#Lista de trás pra frente
nome = list("ARAUJO")
print(nome[::-1])

#append()
numeros.append(11)
print(numeros)

#clear()
lista = ['q',1,3,5,'df',True]
print(lista)
lista.clear()
print(lista)

#copy()
lista = [1,2,3,4,5,6,7,8]
print("Lista original")
print(lista)
lista02 = lista.copy()
print("Lista copiada")
print(lista02)
lista.append(10)
print("Lista original com append de 10")
print(lista)
lista02.append(12)
print("Lista copiada com append de 12")
print(lista02)



#count()
cores = ['vermelho','amarelo','azul','verde','vermelho','verde','vermelho','amarelo','verde']
print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

# Usando o count em uma estrutura condicional
if cores.count("azul") >= 3:
    print("Tem mais que 3")
else:
    print("Tem menos")

# extend()
cores02 = ['vermelho','amarelo','azul','verde','vermelho','verde','vermelho','amarelo','verde']
print('Cores antes do extend')
print(cores02)
novas = ['roxo','preto']
cores02.extend(novas)
print('Cores após do extend')
print(cores02)

#index() passa a primeira ocorrencia
cores02 = ['vermelho','amarelo','azul','verde','vermelho','verde','vermelho','amarelo','verde']
cores02.index('amarelo')

#pop() sem passar o padão tira sempre o ultimo elemento como em uma pilha
print('Antes do pop')
print(cores02)
cores02.pop()
print('Depois do pop, sem passar o paramentro, sai o verde do final')
print(cores02)
cores02.pop(2)
print('Depois do pop, passando o paramentro com base no index, sai a cor azul')
print(cores02)


#remove() remove passando o elemento em si, não pelo index, remove apenas a primeira ocorrencia
cores02 = ['vermelho','amarelo','azul','verde','vermelho','verde','vermelho','amarelo','verde']
print('Antes do remove')
print(cores02)
cores02.remove('amarelo')
print('Depois do remove')
print(cores02)

#removendo mais de um item da lista com o remove
cores02 = ['vermelho','amarelo','azul','verde','vermelho','verde','vermelho','amarelo','verde','vermelho']
quant = cores02.count('vermelho')


while quant > 0:
    cores02.remove('vermelho')
    quant -= 1

print("cores sem os vermelhos")
print(cores02)

#reverse() serve para transpor a lista de trás pra frente como no slice[::-1]
print("Lista de cores normal")
print(cores02)
print(cores02.reverse()) #retorna none porque modifica a lista original
print(cores02)

# sort() serve para onder a lista
lista = ['prstuv','ab','abc','jlmn']
print(lista.sort())#retorna none porque modifica a lista original
print(lista)

#parametros dentro do sort()
lingua = ['python','c','java','c#','ruby','javaScript','cobol']
#sort normal
print(lingua)
lingua.sort()
print(lingua)
#reverse
lingua.sort(reverse=True)
print(lingua)
#key junto com lambda
lingua.sort(key=lambda x:len(x))
print(lingua)
#key junto com lambda e reverse
lingua.sort(key=lambda x:len(x), reverse=True)
print(lingua)

#podemos usar o sorted() função built-in do python
lingua = ['python','c','java','c#','ruby','javaScript','cobol']
sorted(lingua, key=lambda x:len(x), reverse=True)
