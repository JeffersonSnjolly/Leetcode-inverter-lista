import random
import string

def geradorDeSenha(len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    point_options = string.punctuation
    options = ascii_options + number_options + point_options
    aux = ""
    for i in range(0, len_pass):
        digit  = random.choice(options)
        aux = aux + digit
        
    return aux



choice_user = input("Digite a quantidade de caracteres para criar a senha.\n")
if choice_user.isdigit():
    choice_user = int(choice_user)
    senha  = geradorDeSenha(choice_user)
    print(f"Senha gerada: {senha}")