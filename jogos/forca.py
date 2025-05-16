def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    erros = 0 

    while (not enforcou and  not acertou):
        
        chute = input("Qual é a letra?")
        chute = chute.strip().upper()
        
        if (chute in palavra_secreta):

         index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
            index = index + 1
            
    else:
         erros = erros + 1 
            
         enforcou = erros = 10 
         acertou = "_" not in letras_acertadas
         print(letras_acertadas)
         
         if (acertou):
             print ("voce ganhou!!")
         else:
             print("voce perdeu, seu lixo!")
             

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
