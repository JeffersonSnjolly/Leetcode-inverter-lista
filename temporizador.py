import time


tempo = input("Digite o tempo em segundos:\n")
if tempo.isdigit:
    tempo = int(tempo)


while tempo:
    minuto, segundo = divmod(tempo, 60)
    print("{:02d}:{:02d}".format(minuto, segundo), end='\r')
    time.sleep(1)
    tempo -=1
    
print("Fim do tempo.") 