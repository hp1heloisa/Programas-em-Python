jogadorA = str(input("Jogador A digite a sua escolha: "))
jogadorB = str(input("Jogador B digite a sua escolha: "))
if(jogadorA == jogadorB):
  print("Empate!")
elif(jogadorA == "pedra"):
  if(jogadorB == "papel"):
    print("Jogador B venceu!")
  else: 
    print("Jogador A venceu!")
elif(jogadorA == "papel"):
  if(jogadorB == "tesoura"):
    print("Jogador B venceu!")
  else:
    print("Jogador A venceu!")
elif(jogadorA == "tesoura"):
  if(jogadorB == "papel"):
    print("Jogador A venceu!")
  else:
    print("Jogador B venceu!")              
   