from random import randint
print("""
    Vamos brincar de Pedra-papel-tesoura-lagarto-Spock?
    É fácil, eu escolho uma arma e você escolhe outra. Quem marcar 3 pontos vence. """)
pontopc = 0   
ponto1 = 0
x=1


dicionario = {"1": "PEDRA",
              "2": "PAPEL",
              '3':'TESOURA',
              '4':'LAGARTO', 
              '5':'SPOCK'}
              
while True:
      if ponto1 == 3:
          break
      elif pontopc == 3:
          break
      number1 = randint(1,5)
      number = str(number1)
      print("Rodada:", x)
      print("Computador:", pontopc)
      print("Você:", ponto1)
      g=input("""Escolha sua arma: Pedra    (1)
                  Papel    (2)
                  Tesoura  (3)
                  Lagarto  (4)        
                  Spock    (5)

              (Digite o número referente a sua arma):""").strip().upper()
     
      print(" ")
      if g in dicionario:
          
       c= number
       print("Você escolheu %s e eu escolhi %s" % (dicionario[g], dicionario[c]))
       if c==g:
          print("Empate!")       
       elif g=="1":
           if number1 == 2 or number1 == 5:                             
               print("Computador venceu esta rodada")
               pontopc+=1       
           else:                     
            print("Você venceu esta rodada")          
            ponto1+=1
       elif g=="2":
           if number1 == 3 or number1 == 4:
               print("Computador venceu esta rodada")
               pontopc+=1
           else:
               print("Você venceu esta rodada")
               ponto1+=1
       elif g=="3":
           if number1 == 1 or number1 == 5:
               print("Computador venceu esta rodada")
               pontopc+=1
           else:
               print("Você venceu esta rodada")
               ponto1+=1
       elif g=="4":
           if number1 == 1 or number1 == 3:
               print("Computador venceu esta rodada")
               pontopc+=1
           else:
               print("Você venceu esta rodada")
               ponto1+=1
       elif g=="5":
           if number1 == 2 or number1 == 4:
               print("Computador venceu esta rodada")
               pontopc+=1
           else:
               print("Você venceu esta rodada")
               ponto1+=1 
       
      else:
          print("ERRO")
          print("Digite um número de 1 a 5")
      x = x + 1
      print("")
print("Fim de jogo.")
print("Computador:", pontopc)
print("Você:", ponto1)  
if pontopc == 3:
    print("Computador venceu!")
else:
    print("Você venceu!")

