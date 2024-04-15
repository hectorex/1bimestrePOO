class Pokemon:
  def __init__ (self, nome, overall, tipo, hp, spd, kg, ataque, defesa, altura):
    self.nome = nome
    self.overall = overall
    self.tipo = tipo
    self.hp = hp
    self.spd = spd
    self.kg = kg
    self.ataque = ataque
    self.defesa = defesa
    self.altura = altura

  def exibirCarta (self):
    print ("\nNome:", self.nome,
    "\nOverall:", self.overall,
    "\nTipo:", self.tipo,
    "\nHp:", self.hp,
    "\nSpd:", self.spd,
    "\nKg:", self.kg,
    "\nAtaque:", self.ataque,
    "\nDefesa:", self.defesa,
    "\nAltura:", self.altura)

  def compararCartas(self, pokemon2): 
    atributo = input("Qual atributo você deseja comparar?\n[1] Overall\n[2] Hp\n[3] Spd\n[4] Kg\n[5] Ataque\n[6] Defesa\n[7] Altura\nR: ")
    if atributo == "1":
      if self.overall > pokemon2.overall:
        print(f"{self.nome} ganhou por ter o maior Overall, Parabens!!")
      elif self.overall == pokemon2.overall:
        print("Empate")
      else: 
        print (f"{pokemon2.nome} ganhou por ter o maior Overall")

    elif atributo == "2":
      if self.hp > pokemon2.hp:
        print(f"{self.nome} ganhou por ter o maior Hp, Parabens!!")
      elif self.hp == pokemon2.hp:
        print("Empate")
      else: 
        print (f"{pokemon2.nome} ganhou por ter o maior Hp")

    elif atributo == "3":
      if self.spd > pokemon2.spd:
        print(f"{self.nome} ganhou por ter mais Speed, Parabens!!")
      elif self.spd == pokemon2.spd:
        print("Empate")
      else: 
        print (f"{pokemon2.nome} ganhou por ter mais Speed")

    elif atributo == "4":
      if self.kg > pokemon2.kg:
        print(f"{self.nome} ganhou por ter mais Kg, Parabens!!")
      elif self.kg == pokemon2.kg:
        print("Empate")
      else: 
        print (f"{pokemon2.nome} ganhou por ter mais Kg")

    elif atributo == "5":
      if self.ataque > pokemon2.ataque:
        print(f"{self.nome} ganhou por ter o maior Ataque, Parabens!!")
      elif self.ataque == pokemon2.ataque:
        print("Empate")
      else: 
        print (f"{pokemon2.nome} ganhou por ter o maior Ataque")

    elif atributo == "6":
      if self.defesa > pokemon2.defesa:
        print(f"{self.nome} ganhou por ter a maior Defesa, Parabens!!")
      elif self.defesa == pokemon2.defesa:
        print("Empate")
      else: 
        print (f"{pokemon2.nome} ganhou por ter a maior Defesa")

    elif atributo == "7":
      if self.altura > pokemon2.altura:
        print(f"{self.nome} ganhou por ter a maior Altura, Parabens!!")
      elif self.altura == pokemon2.altura:
        print("Empate")
      else: 
        print (f"{pokemon2.nome} ganhou por ter a maior Altura")
