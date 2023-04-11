pag = input().split()
dicent = {}
dicsaid = {}
for i in range(len(pag)):
  dicent[pag[i]] = []
  dicsaid[pag[i]] = []
lig = input()
while not(lig.isdigit()):
  lig = lig.split()
  if lig[0]!=lig[2]:
    dicent[lig[0]].append(lig[2])
    dicsaid[lig[2]].append(lig[0])
  lig = input()
for i in range(len(pag)):
  certo = []
  for j in dicent[pag[i]]:
    if j not in certo:
      certo.append(j)
  certo.sort()    
  dicent[pag[i]] = certo    
for i in range(len(pag)):
  certo = []
  for j in dicsaid[pag[i]]:
    if j not in certo:
      certo.append(j)
  certo.sort()    
  dicsaid[pag[i]] = certo    
for i in range(len(pag)):
  print(pag[i], "->",dicent[pag[i]])
  print(dicsaid[pag[i]], "->",pag[i])
lig = int(lig)
valoresant = {}
valoresatua = {}
inicial = 1/len(pag)
fat = (1-0.875)/len(pag)
print("PageRank (passo ",0,")", sep = "")
for i in range(len(pag)):
  print(pag[i], ": ", format(inicial, ".3f"), sep = "")
  valoresant[pag[i]] = inicial
for i in range(1,lig+1):
  print("PageRank (passo ",i,")", sep = "")
  for j in pag:
    soma = 0
    for k in dicsaid[j]:
      x = valoresant[k]/len(dicent[k])
      soma = soma + x
    valoresatua[j] = soma*0.875 + fat
  for j in pag:  
    print(j, ": ", format(valoresatua[j], ".3f"), sep = "")
    valoresant[j] = valoresatua[j]  





