def obrigarResposta(msg: str, respostasAceita):
    respostaObrigado = input(msg)

    while respostaObrigado not in respostasAceita:
        respostaObrigado = input("Erro!\n " + msg)
        
    return respostaObrigado


def textoAnimado(string):
    import time, sys

    for letra in string:
        print(letra, end='')
        sys.stdout.flush()
        time.sleep(0.03)
         
