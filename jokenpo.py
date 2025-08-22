import random
import os

# r = pedra, p  = papel t = tesoura

possiveis = ['r','p','t']

v_pc = 0
v_user = 0 
partidas = 0
empates = 0

while True:
    print('*'*49)
    print("*"*20+"JO-KEN-PO"+"*"*20)
    print('*'*49)
    print(f"Vitorias usuario : {v_user}")
    print(f"Vitorias android : {v_pc}")
    print(f"Partidas jogadas : {partidas}")
    print(f"Empates : {empates}")
    print('*'*49)
    
    user = input("r -> pedra, p -> papel, t -> tesoura, x- >sair: ").lower()
    
    if user in possiveis:
        choice_pc = random.randint(0,2)
        if user == possiveis[choice_pc]:
            print("Empate.")
            empates +=1
            partidas += 1
            input("Enter")
            os.system('cls')
        elif user == "r" and possiveis[choice_pc] == 't':
                print(f"Vitoria do usuario {user} x {possiveis[choice_pc]}")
                v_user += 1
                partidas += 1
                input("Enter")
                os.system('cls')
        elif user == "p" and possiveis[choice_pc] == 'r':
                print(f"Vitoria do usuario {user} x {possiveis[choice_pc]}")
                v_user += 1
                partidas += 1
                input("Enter")
                os.system('cls')
        elif user == "t" and possiveis[choice_pc] == 'p':
                print(f"Vitoria do usuario {user} x {possiveis[choice_pc]}")
                v_user += 1
                partidas += 1
                input("Enter")
                os.system('cls')
        else:
            print(f"Vitoria do Android {possiveis[choice_pc]} X {user}")
            v_pc += 1
            partidas += 1
            input("Enter")
            os.system('cls')
            
                
    elif user == "x":
        break
    else:
        print("deu ruim")
        break
os.system('cls')
print('*'*49)
print("*"*20+"JO-KEN-PO"+"*"*20)
print('*'*49)  
print("Resultado da partida.")
print(f"Vitorias usuario : {v_user}")
print(f"Vitorias android : {v_pc}")
print(f"Empates : {empates}")
print(f"Partidas jogadas : {partidas}")

print("Goodby.")

