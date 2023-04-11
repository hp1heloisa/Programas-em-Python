aprov = True
peso = float(input(""))
idade = int(input(""))
if(idade>=16 and idade<18):
  documento = str(input("")) 
cbs = str(input(""))
udi = str(input(""))
pd = str(input(""))
if(pd == "N"):
  mdud = int(input(""))
  du12m = int(input(""))
sb = str(input(""))
if(sb == "F"):
  grav = str(input("")) 
  leite = str(input("")) 
  if(leite == "S"):
    ibsamamen = int(input(""))
print("Peso:",peso)
print("Idade:",idade)
if(idade>=16 and idade<18):
  print("Documento de autorizacao:",documento)
print("Boa saude:",cbs)
print("Uso drogas injetaveis:",udi)
print("Primeira doacao:",pd)  
if(pd == "N"):
  print("Meses desde ultima doacao:",mdud)
  print("Doacoes nos ultimos 12 meses:",du12m)
print("Sexo biologico:",sb)
if(sb == "F"):
  print("Gravidez:",grav)
  print("Amamentando:",leite)
  if(leite == "S"):
    print("Meses bebe:",ibsamamen)
imp = "Impedimento:"    
if(peso<50):
  print(imp,"abaixo do peso minimo.")
  aprov = False
if(idade<16):
  print(imp,"menor de 16 anos.") 
  aprov = False   
if(idade>=16 and idade<18 and documento == "N"):
  print(imp,"menor de 18 anos, sem consentimento dos responsaveis.")  
  aprov = False    
if(idade>60 and idade<=69 and pd == "S"):
  print(imp,"maior de 60 anos, primeira doacao.")
  aprov = False  
if(idade>69):
  print(imp,"maior de 69 anos.")  
  aprov = False  
if(cbs == "N"):
  print(imp,"nao esta em boa saude.")  
  aprov = False  
if(udi == "S"):
  print(imp,"uso de drogas injetaveis.")
  aprov = False  
if(sb == "M" and pd == "N" and mdud<2):
  print(imp,"intervalo minimo entre as doacoes nao foi respeitado.")
  aprov = False  
if(sb == "M" and pd == "N" and du12m>=4):
  print(imp,"numero maximo de doacoes anuais foi atingido.")
  aprov = False     
if(sb == "F" and pd == "N" and mdud<3):
  print(imp,"intervalo minimo entre as doacoes nao foi respeitado.")
  aprov = False  
if(sb == "F" and pd == "N" and du12m>=3):
  print(imp,"numero maximo de doacoes anuais foi atingido.")  
  aprov = False       
if(sb == "F" and grav == "S"):
  print(imp,"gravidez.")
  aprov = False  
if(sb == "F" and leite == "S" and ibsamamen<12):
  print(imp,"amamentacao.")  
  aprov = False  
if aprov:
  print("Procure um hemocentro para triagem completa.")  

   
