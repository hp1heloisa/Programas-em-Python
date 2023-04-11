distAB = float(input())
vA = float(input())
vB = float(input())
pontoD = float(input())
compB = float(input())
tA = (pontoD/vA)*60
print(format(tA, '.2f'),"min")
tB = (distAB-pontoD)/vB
tBmin = tB*60
Bkm = compB/1000
tcompB = (Bkm/vB)*60
totalB = tBmin+tcompB
print(tA<=totalB)

