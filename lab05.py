moeda = str(input(""))
data = str(input(""))
vc, vv = map(float, input().split())
mincomp = None
maxvend = None
somvend = 0
somcomp = 0
contador = 0
subsomc = 0
subsomv = 0
while vc!=0 and vv!=0:
  if mincomp == None or vc<mincomp:
    mincomp = vc
  if maxvend == None or vv>maxvend:
    maxvend = vv  
  somcomp = somcomp + vc
  somvend = somvend + vv
  contador = contador + 1
  vc, vv = map(float, input().split())    
  if contador<=5:
    subsomc = somcomp 
    subsomv = somvend
print("Moeda:",moeda)
print("Data:",data)
print("Valor minimo para compra:",format(mincomp,".4f"))
print("Valor maximo para venda:",format(maxvend,".4f"))
print("Medias das cinco cotacoes mais recentes: {0:.4f} {1:.4f}".format(subsomc/5,subsomv/5))
print("Medias do historico: {0:.4f} {1:.4f}".format(somcomp/contador,somvend/contador))