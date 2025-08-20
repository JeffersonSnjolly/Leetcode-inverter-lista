import random
import os
import time

# r:pedra, t:tesoura, p:papel
v_pc = 0
v_user = 0

while True:
    start = input("Aperte C para continuar: \n").lower()
    if start != "c":
        break
    
    print("Jokenpo...\n")
    op = input("r ->pedra, t -> tesoura, p -> papel\n").lower()
    movimentos_pc = ["r","t","p"]
    choice_pc = random.randint(0,2)
    if op == movimentos_pc[choice_pc]:
        print("Empate")
        time.sleep(4)
        os.system("cls")
    elif op == "r" and movimentos_pc[choice_pc] == "t":
        print("Vitoria do usuario!")
        print(f"{op} ganha de {movimentos_pc[choice_pc]}")
        v_user +=1
        time.sleep(4)
        os.system("cls")
    elif op == "t" and movimentos_pc[choice_pc] == "p":
        print("Vitoria do usuario!")
        print(f"{op} ganha de {movimentos_pc[choice_pc]}")
        v_user +=1
        time.sleep(4)
        os.system("cls")
    elif op == "p" and movimentos_pc[choice_pc] == "r":
        print("Vitoria do usuario!")
        print(f"{op} ganha de {movimentos_pc[choice_pc]}")
        v_user +=1
        time.sleep(4)
        os.system("cls")
    else:
        print("Vitoria do PC!")
        print(f"{movimentos_pc[choice_pc]} ganha de {op}")
        v_pc +=1
        time.sleep(4)
        os.system("cls")

    
print(f"Vitoria PC \n{v_pc}")
print(f"Vitoria usuario \n{v_user}")
print("goodby!")
