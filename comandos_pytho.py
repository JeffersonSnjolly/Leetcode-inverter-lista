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