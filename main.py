# 2º Ano B Vespertino Informática
# -------------------------------- Alunos/Programadores ----------------------------
# ------------------------------  André Luís Bento Ferreira -----------------------
# ------------------------------  Celso Hector Silva Sales ------------------------
# -----------------------------  Luiz Felipe Macedo Alencar de Menezes -------------
# -----------------------------  Paulo Gabriel Viera Alves -------------------------

from poke import Pokemon
import random
from time import sleep

rayquaza = Pokemon("Rayquaza", 99, "Dragão Voador", 105, 95, 206.5, 150, 90, 7.0)
urshifu =  Pokemon("Urshifu", 72, "Água", 96, 89, 92.0, 85, 74, 1.9)
pichu =   Pokemon("Pichu", 56, "Elétrico", 20, 60, 2.0, 40, 15, 0.3)
empoleon =   Pokemon("Empoleon", 84, "Água", 84, 60, 84.0, 86, 88, 1.7)
mewtwo =  Pokemon("Mewtwo", 99, "Psíquico", 106, 130, 122.0, 110, 90, 2.0)
pikachu =   Pokemon("Pikachu", 64, "Elétrico", 35, 90, 6.0, 55, 40, 0.4)
froakie =   Pokemon("Froakie", 60, "Água", 41, 71, 7.0, 56, 40, 0.3)
deino =  Pokemon("Deino", 65, "Dragão | Sombrio", 52, 38, 17.0, 65, 50, 0.8)

def embaralhar():
  print("Embaralhando...")
  sleep(1)
  pokemons = [rayquaza,urshifu,pichu,empoleon,mewtwo,pikachu,froakie,deino]
  global pokemon1 
  global pokemon2
  #sorteando pokemon do p1
  pokemon1 = random.choice(pokemons)

  #sorteando pokemon do p2
  pokemon2 = random.choice(pokemons)

  #evitando repetição de pokemons
  while pokemon1 == pokemon2:
      pokemon1 = random.choice(pokemons)     
  print ("Embaralhado!")
  return pokemon1, pokemon2

def cor(texto):
  print("\033[1m" + texto + "\033[0m")
def menus():
  print("="*10, " " + "Super Trunfo - Pokemon" + " ", "="*10, "\n")

  cor("1 - Jogar\n2 - Creditos\n3 - Sair")
  modo = int(input("Selecione, de acordo com o número, o que deseja: "))

  while modo < 1 or modo > 3:
      modo = int(input("Valor inválido! Selecione entre 1 e 3: "))

    #Se for 3, sai do programa
  if modo == 3:
     print("Até mais! :D")
    #Se for 2, mostra os créditos
  elif modo == 2:

    cor("\nParticipantes do grupo:")
    print(
          "André Luís;\nCelso Hector;\nLuiz Felipe;\nPaulo Gabriel."
      )

    cor("\n1 - Jogar\n2 - Sair")

    modo = int(input("Selecione, de acordo com o número, o que deseja: "))

    while modo != 1 or modo != 2:
      modo = int(input("Valor inválido! Selecione 1 ou 2: "))

      if modo == 2:
          print("Até mais! :D")
          exit()
      if modo == 1:
          print("\nVamos começar!")
          sleep (0.5)
          embaralhar()
          sleep(0.5)
          res2 = 0
          while res2 != 3:
              res2 = int(input("\n1 - Exibir Carta\n2 - Comparar Carta\n3 - Sair do Progama\nR: "))
              if res2 == 1:
                  Pokemon.exibirCarta(pokemon1)


              elif res2 == 2:
                  print ("O pokemon de seu oponente é:", pokemon2.nome)
                  sleep (0.75)
                  Pokemon.compararCartas(pokemon1, pokemon2)

              elif res2 == 3:

                  print ("Entendi, Muito obrigado\nTchau ;)")
                  exit()


              elif modo == 3:
                  cor("\nFechando o jogo...")
                  exit()

      else:
        print ("Numero inválido!!")


  elif modo == 1:
    print("\nVamos começar!")
    sleep (0.5)
    embaralhar()
    sleep(0.5)
    res2 = 0
    while res2 != 3:
        res2 = int(input("\n1 - Exibir Carta\n2 - Comparar Carta\n3 - Sair do Progama\nR: "))
        if res2 == 1:
            Pokemon.exibirCarta(pokemon1)


        elif res2 == 2:
            print ("O pokemon de seu oponente é:", pokemon2.nome)
            sleep (0.75)
            Pokemon.compararCartas(pokemon1, pokemon2)

        elif res2 == 3:

            print ("Entendi, Muito obrigado")
            sleep (1)
            print ("Tchau ;)")
            exit()


        elif modo == 3:
            cor("\nFechando o jogo...")
            exit()

        else:
          sleep (0.5)
          print ("\nValor Inválido, selecione (1, 2 ou 3)")
          sleep (0.5)
menus ()