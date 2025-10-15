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


#funçõs

def exibir_mensagem():
    print("Olá mundo")
    
def exibir_mensagem_2(nome):
    print(f"Olá {nome}")

def exibir_mensagem_3(nome = "Tamyres"):
    print(f"Olá {nome}")


#chamando as funções
exibir_mensagem()
#Argumento obrigatório 
exibir_mensagem_2("jeff")
#Vem como o nome Tamyres como padrão
exibir_mensagem_3()
#podemos alterarna chamada
exibir_mensagem_3(nome='Maria')

# O podemos retorna um None ou multiplos valores
def soma(*numeros):
    return sum(numeros)

def ante_e_sucess(numero):
    ante = numero -1
    sucess = numero + 1
    return ante, sucess
def func_03():
    print("olá mundo")

print(soma(1,2,3,4,5,6,7,8,9))
print(ante_e_sucess(10))
print(func_03())

#Argumentos Nomeados

def carros_01(marca,modelo,ano,placa):
    
    print(f"Carro inserido com sucesso! Marca:{marca} / Modelo:{modelo} / Ano:{ano} / Placa:{placa}")

#possibilidades para iserir os dados
#sem nomear
carros_01("Fiat",'Fast Back',2025,'abc-1234')

#nomeados
carros_01(marca="BMW",modelo="X6 serie-M",ano=2024,placa='cde-6666')

#Passando como um dicionario
carros_01(**{"marca":"Porche","modelo":"911 Carreira GT","ano":2022,"placa":"sos-9874"})

#*args e **kargs
#args retorna um tupla
#**kargs retorna um dicionario

def exibir_poema(data_extenso, *args, **kargs):
    texto = "\n".join(args) 
    meta_dados = "\n".join([f"{chave.upper()}: {valor}" for chave,valor in kargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    return mensagem

#Declarando o peoma
poema = exibir_poema(
    "Sexta feira 10 de Outubro, São paulo",
    "Rosas são belas.",
    "E o sangue, escorre delas.",
    "Rosas são belas.",
    "E na morte, recebe elas.",
    Autor="Jefferson",Ano=2025
)

# Chamando o poema
print(poema)


# Paramentros especiais
# Obrigando a passar nomeados ou não usando o /
# Usando o / fica opcional

def carros3(modelo,marca,/,ano,placa):
    mensagem = f"{modelo}, {marca}, {ano}, {placa}"
    return mensagem

#Válido
car1 = carros3('palio','fiat',ano=2010,placa='abs-2233')# Correto, os dois primeiros paramentros não devem ser nomeados
print(car1)

# Inválido
car2 = carros3(modelo='palio',marca='fiat',ano=2010,placa='abs-2233') # Gera um erro, os dois primeiros paramentros não devem ser nomeados
print(car2)

# Usando * todos os valores são obrigatorios de serem nomeados
def carros4(*,modelo,marca,ano,placa):
    mensagem = f"{modelo}, {marca}, {ano}, {placa}"
    return mensagem

# Inválido
car3 = carros4('palio','fiat',ano=2010,placa='abs-2233') # Gera um erro, os dois primeiros paramentros não devem ser nomeados
print(car1)

#Válido 
car4 = carros4(modelo='palio',marca='fiat',ano=2010,placa='abs-2233') # Correto, os dois primeiros paramentros não devem ser nomeados
print(car4)

# Hibridos com / e *
def carros5(modelo,marca,/,ano,*,placa,tipo):
    mensagem = f"{modelo}, {marca}, {ano}, {placa}, {tipo}"
    return mensagem

car5= carros5('gol','volkswagen',2012,placa='dgf-4455',tipo='Etanol')
print(car5)


# Objetos de primeira classe
# passando a função como objeto de primeira classe

def somar(a,b):
    soma = a + b
    return soma

def subtrair(a,b):
    sub = a - b
    return sub

def nova_func(a,b, funcao):
    resultado = funcao(a,b)
    return f" o Resultado de {a} e {b} = {resultado}"

a1 = nova_func(10,5,somar) # aqui a função somar não recebe os paranteses (), é usada como objeto de primeira classe
print(a1)
# Assim podemos a nova_func com resultados diferentes dependendo do objeto de primeira classe no passado
a2 = nova_func(5,2,subtrair)
print(a2)

#podemos atribuir esse comportamento para uma variavel
op = somar
print(op(5,2))


# Escopo local e global
# Utilize a palavra global apesar de não ser uma boa prática

# exemplo 01
salario = 2000
def bonus(valor):
    global salario
    salario += valor
    return salario


print(salario)

bonus(500)

print(salario)



# exemplo 02
nome = "Jeff"

def novo_nome():
    nome = "Lucas"
    print(nome)
    
print(nome)

novo_nome()


#Exemplo 03
#listas são sempre interaiveis imutaveis por padrão altera no global mesmo não passando a palavra reservada global
lista = [1]

def alterando_lista(lista):
    lista.append(2)
    lista.append(3)
    

alterando_lista(lista)

print(lista)

#Exemplo 04


def alterando_lista2(lista):
    lista2 = lista.copy()
    lista2.append(2)
    lista2.append(3)
    

alterando_lista(lista)

alterando_lista2(lista)


# Decoradores
# Funções em python são objetos e podem ser tratadas como funções de primeir linha
# Sendo chamada por outras funções sem uso caracteristicos dos parenteses ()
# inner function são funções dentro de funções 
# podemos retornar funçoes

#ex
def calcular(operador):
    def somar(a,b):
        r = a+b
        return r
    def subtrair(a,b):
        r = a-b
        return r
    if operador == "+":
        return somar # retorna a função
    else:
        return subtrair
    
print(calcular("-")(4,3)) #precisamos passar o parametro adicional de "somar" ou "subtrair" no caso com os parenteses adicionais.

# Função de primeira
def dizer_oi(nome):
    return f"Oi {nome}"

def incentivando(nome):
    return f"oi {nome}, continue estudando python que um dia vai dar certo."

def manda_mensagem(funcao, nome):
    return funcao(nome)

print(manda_mensagem(dizer_oi, "Paula"))
print(manda_mensagem(incentivando, "Bia"))

# inner function
def externa():
    print("Esrevendo na função externa.")
    
    def interna01():
        print("Esrevendo a interna01")
        
    def interna02():
        print("Esrevendo a interna01")
    
    interna01()
    interna02()
    
externa()

# Primeiro decorador
def decorador(funcao):
    def envelope():
        print("Faz algo antes")
        funcao()
        print("Faz algo depois")
        
    return envelope #sempre sem parentes

def ola_mundo():
    print("Olá mundo.")
    
ola_mundo = decorador(ola_mundo) # usando o decorador
ola_mundo()

# Usando o açucar sintático o python podemos @

def decorador(funcao):
    def envelope():
        print("Faz algo antes")
        funcao()
        print("Faz algo depois")
        
    return envelope #sempre sem parentes

@decorador #Colocando o @ usamos o decorador
def ola_mundo():
    print("Olá mundo.")
    
#ola_mundo = decorador(ola_mundo) # usando o decorador
ola_mundo()

# Decorador com parametro/argumento
def duplica(funcao):
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
        funcao(*args, **kwargs)
    return envelope

@duplica
def tecnologia(nome):
    print(f"Estou aprendendo a programar em {nome}")
    
    
tecnologia("Python")

#retornando dentro do envelop
def retorna_msn(funcao):
    def envelope(*args, **kwargs):
        aux = funcao(*args, **kwargs)
        return aux # criando esse retorno podemos dar um retorno na função decorada
    return envelope
    
@retorna_msn
def nova_msn(tec):
    return f"Estou estudado {tec.upper()}"

linguagen = nova_msn("python")
print(linguagen)

print(nova_msn.__name__)

# Intropecção, retorona o nome verdadeiro da funão decorocada, e não o envelope
import functools #precisamos fazer o import

def retorna_filme(funcao):
    @functools.wraps(funcao) # Chame esse decorador para manter o nome da função decorada
    def envelope(*args, **kwargs):
        aux = funcao(*args, **kwargs)
        return aux # criando esse retorno podemos dar um retorno na função decorada
    return envelope
    
@retorna_filme
def novo_filme(nome):
    return f"Estou assistindo o {nome.title()}, essa noite."

filme01 = novo_filme("gladiador")
print(filme01)

print(novo_filme.__name__)


#iteradores 
#interador é um objeto que contém um número contável de valores que podem ser iterados.
# dois metodos especiais __iter__() e __next__()
#criando um interavel

class Meu_iteravel:
    def __init__(self, numeros : list[int]):
        self.numeros = numeros
        self.contador = 0
        
    def __iter__(self):
        return self
    def __next__(self):
        try:
            num = self.numeros[self.contador]
            self.contador +=1
            return num *2
        except IndexError:
            raise StopIteration #Sempre ter o stop interation.
        
        

for i in Meu_iteravel([1,2,3,4]):
    print(i)
# Geradores são tipos especiais de iteradores
# Não armazenam todos os seus valores na memoria
# São definidos usando funções regulares
# Para retorna os valores não utilizam o "return" e sim o "yield"
# Geradores podem colheitar elemento por elemento e quardar em memória sem precisar,
# Alocar toda a base ou lista.

# Característica de geradores
# Uma vez que o item é consumido, ele é esquecido e não pode mais ser acessado
# O estado interno de um gerador é mantido entre chamadas
# A execução de um gerador é pausada na declaração do yield
# e retornada dai na próxima vez que ele for chamado 


# ex

def meu_gerador(*numeros):
    for num in numeros:
        yield num *2
    
for i in meu_gerador(1,2,3,4,5):
    print(i)


#manipulando arquivos

"""Tipos de aberturas de arquivos"""

# Para ler (read)

file = open("texto01.txt",'r')
aux = file.read()
file.close()
print(aux)

# Para escrever (write)

texto = "Estou cada dia mais melhorando em programação."
file = open("texto01.txt", "w")
file.write(texto)
file.close() 

#lendo novamente

file = open("texto01.txt",'r')
aux = file.read()
file.close()
print(aux)

# Para realizar um append

novo_texto = "\nEstudo de python continuo, vai ajudar muito."
file = open("texto01.txt","a")
file.write(novo_texto)
file.close()

#lendo novamente

file = open("texto01.txt",'r')
aux = file.read()
file.close()
print(aux)

# Um novo append

novo_texto = "\nEssa terceira linha é um loren."
file = open("texto01.txt","a")
file.write(novo_texto)
file.close()


#lendo novamente como readline

file = open("texto01.txt",'r')
aux = file.readline() #ler uma linha por vez, da pra usar o for junto ao len(file)
file.close()
print(aux)

#lendo novamente com readlines

file = open("texto01.txt",'r')
aux = file.readlines() # Transfoma cada linha em cada posição de uma lista.
file.close()
print(aux)

# Gereanciando arquivos
import os
import shutil
from pathlib import Path #Para conseguir o caminho dinamico

#print(__file__) retorna o caminho do diretorio
#ROOT_PATH = Path(__file__) não funciona no notebook
#print(ROOT_PATH.parent)

#Criar um diretório
#os.mkdir("exemplo")

#Renomear um arquivo
#os.rename("old_name.txt", "new_name.txt")

#removendo um arquivo
#os.remove("texto.txt")

#mover um arquivo
#shutil.move("soucer.txt", "destination.txt")


#EX
# ROOT_PATH = Path(__file__).parent


#os.mkdir(ROOT_PATH / "novo-diretorio")

# file = open(ROOT_PATH / "novo_arquivo.txt", "w")
# file.close()

# os.rename(ROOT_PATH / "novo_arquivo.txt", ROOT_PATH / "alterado.txt")

#os.remove(ROOT_PATH / "alterado.txt")

#shutil.move(ROOT_PATH / "novo_arquivo.txt", ROOT_PATH / "novo-diretorio" / "novo_arquivo.txt")

# Tratamento de execeções

# Execeções comuns

#FileNotFoundError -> se não for localizado.

#PermissionError -> quando não tiver permissão.

#IOError -> Erro em geral de entrada e saida

#UnicodeDecodeError -> ao tentar decodificar um arquivo mal codificado

#UnicodeEncodeError -> ao tentar codificar

#IsADirectoryError -> ao tentar abrir um diretório ao invez de um arquivo.

#Teste de arquivo 01

try:
    file = open("nãoExiste.txt", "r")
    file.close()
except FileNotFoundError as exc:
    print(f"Arquivo não encontrado {exc}")
except Exception as exc:
    print(f"Algo de errado não está certo")

#Teste de arquivo 02
try:
    file = open("texto01.txt", "r")
    aux = file.read()
    file.close()
    print(aux)
except FileNotFoundError:
    print("Arquivo não encontrado")

# Boas práticas

# A declaração do with garante que o arquivo será fechado mesmo com execeções.

# ex: with open("arquivo.txt", "r") as arq:
            #aux = arq.read()
            
            
import os
try:
    with open(os.path.join("ttexto01.txt"), 'r') as arq:
        print(f"TEXTO\n{arq.read()}")
except IOError as exc:
    print(f"Tipo do erro: {exc}")

# encoding="utf-8" garante a codificação correta e garante o acentos epecias.
try:
    with open(os.path.join("texto_utf8.txt"), 'w', encoding="utf-8") as arq:
        arq.write("Esse texto tem umolá mundo, e não atoa a união com varios acentos em palavras.")
except IOError as exc:
    print(f"Tipo de erro: {exc}")
    

# Gera esse UnicodeDecodeError
try:
    with open(os.path.join("texto_utf8.txt"), 'r', encoding="ascii") as arq:
        arq.read()
except IOError as exc:
    print(f"Tipo de erro: {exc}")
except UnicodeDecodeError as exc:
    print(f"Tipo de erro: {exc}")

# CSV
import csv
try:
    with open(os.path.join("arquivo.csv"), 'w',  newline='', encoding="utf-8") as arq: # sempre usar o newline em arq CSV
        escritor = csv.writer(arq)
        escritor.writerow(["id","nome"])
        escritor.writerow(['1','Maria'])
        escritor.writerow(['2','João'])
except IOError as exc:
    print(f"Tipo de Erro: {exc}")

try:
    with open(os.path.join("arquivo.csv"), 'r',encoding="utf-8") as arq:
        leitor = csv.reader(arq)
        for row in leitor:
            print(row)
except IOError as exc:        
    print(f"Tipo de Erro: {exc}")


