def arredondar(num):
  if (round(num-round(num,3),4))>=0.0005:
    num = round(num,3)+0.001
  else:
    num= round(num,3)
  return num 
def arredondar1(num):
  if (round(num-round(num,3),3))>=0.0005:
    num = round(num,3)+0.001
  else:
    num= round(num,3)
  return num 
#Atribuição de valores
print("alpha:")
alpha = float(input())
print("beta:")
beta = float(input())
print("sigma:")
sigma = float(input())
print("Feromônio Inicial:")
ferinic = float(input())
print("Q:")
Q = float(input())
print("Número de cidades:")
cidades = int(input())
tabela1 = []
print("Todas as rotas possíveis:")
for i in range(cidades*(cidades-1)):
  tabela1.append([input()])
  for j in range(6):
    tabela1[i].append(0)
print("Distância entre cada cidade:")
for i in range(cidades*(cidades-1)):
  print(tabela1[i][0]+":")
  tabela1[i][1] = float(input())
  tabela1[i][2] = round(1/tabela1[i][1],3)
  tabela1[i][3] = ferinic
  tabela1[i][4] = arredondar((tabela1[i][2]*tabela1[i][3])) #produto do tau com o eta
#Chance de escolher determinado caminho
c = 0  
for i in range(cidades):
  soma = 0
  for j in range(cidades-1):
    soma = soma + tabela1[i+j+c][4]
  for j in range(cidades-1):
    tabela1[i+j+c][5] = round(tabela1[i+j+c][4]/soma,3)
    tabela1[i+j+c][6] = round(tabela1[i+j+c][5]*100,3)
  c = c + cidades - 2
print("Tabela da interação 1:")
for i in tabela1:
  print(i)   #tabela 1 já pronta
#começa a parte de escolher o caminho de cada formiga  
formigas = []
print("Qual será a primeira rota das formigas?")
for i in range(cidades):
  caminho=[]
  tam = 0
  caminho.append(i+1)
  print("F",i+1,":",)
  for j in range(cidades):
    caminho.append(input())
    for k in range(cidades*(cidades-1)):
      if caminho[j+1] in tabela1[k]:
        ind = tabela1[k].index(caminho[j+1])
        tam = tam + tabela1[k][ind+1] #soma para achar a caminhada total de cada formiga
  caminho.append(tam) 
  formigas.append(caminho) #criação da lista com a rota de cada formiga
#parte da primeira atualização do feromonios 
rot = []
rotas = []
def inverter(txt):
  return txt[::-1]
c = 0
for i in range(cidades*(cidades-1)):
  v = tabela1[i][0]
  if not(v in rot) and not(inverter(v) in rot):
    rot.append(v)
    rotas.append([v])
    for j in range(cidades+2):
      rotas[c].append(0)
    c+=1    
#acima contera a tabela, que contém o valor do feromonio em cada rota, que será atualizada após cada formiga depositar seu feromônio, com o valor total para cada rota xy
#a partir daqui caso nao tenha sido obtida a melhor rota iremos começar as próximas interações, até satisfazer a condição do while
condicao = 0 
for i in range(cidades):
  condicao += formigas[i][cidades+1]
intera = 1 #criando a condicao do while
while condicao/cidades != formigas[0][cidades+1]:
  intera += 1
  for i in range(len(rotas)):
    for j in range(cidades*(cidades-1)):
      if rotas[i][0] in tabela1[j]:
        d = tabela1[j][3]
    rotas[i][1] = (1-sigma)*d #colocando o valor inicial de feromonio em cada rota
  for i in range(len(rotas)):
    g = rotas[i][0]
    for j in range(len(formigas)):
      if g in formigas[j] or inverter(g) in formigas[j]:
        form = Q/(formigas[j][cidades+1])
        rotas[i][j+2] = arredondar1(form)
        rotas[i][cidades+2] = rotas[i][cidades+2] + rotas[i][j+2]
    rotas[i][cidades+2] += rotas[i][1]
    rotas[i][cidades+2] = arredondar1(rotas[i][cidades+2]) #acima, calculo do feromonio depositado em cada rota
  #abaixo, atualização da tabela de interações com o valor do feromonio  
  for i in range(len(rotas)):
    g = rotas[i][0]
    for j in range(cidades*(cidades-1)):
      if g in tabela1[j] or inverter(g) in tabela1[j]:
        tabela1[j][3] = rotas[i][cidades+2]  
  for i in range(cidades*(cidades-1)):
    tabela1[i][4] = round(tabela1[i][2]*tabela1[i][3],3) #atualização do produto do tau com o eta
  #agora é a atualizacao do novo valor da probabilidade   
  c = 0  
  for i in range(cidades):
    soma = 0
    for j in range(cidades-1):
      soma = soma + tabela1[i+j+c][4]
    for j in range(cidades-1):
      tabela1[i+j+c][5] = round(tabela1[i+j+c][4]/soma,3)
      tabela1[i+j+c][6] = round(tabela1[i+j+c][5]*100,3)
    c = c + cidades - 2 
  print("Tabela da interação",intera)  
  for i in tabela1:
    print(i)    
  print("Rota da interação",intera-1)  
  for i in formigas:
    print(i)
  print("Ainda não sabemos a melhor rota... qual serão as próximas rotas?" ) 
  #nova escolha de rotas e caso essa escolha satisfaça o while teremos as melhores rotas
  for i in range(cidades):
    tam = 0 
    print("F",i+1,":",)
    for j in range(cidades):
      formigas[i][j+1] = input()
      for k in range(cidades*(cidades-1)):
        if formigas[i][j+1] in tabela1[k]:
          ind = tabela1[k].index(formigas[i][j+1])
          tam = tam + tabela1[k][ind+1]
    formigas[i][cidades+1] = tam 
  condicao = 0 
  for i in range(cidades):
    condicao += formigas[i][cidades+1] #renovando a condicao do while   
print("Muito bem! Na interação",intera,"descobrimos a melhor rota:") 
for i in formigas:
  print(i)





















