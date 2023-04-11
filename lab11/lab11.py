pa = int(input())
pb = int(input())
import csv
arquivo = csv.reader(open("dados.csv"))
for fileira in arquivo:
  div = pa + pb/float(fileira[0])
  delta = float(fileira[1]) - float(fileira[2])
  difere = div - float(fileira[3])
  fileira.insert(3,delta)
  fileira.append(div)
  fileira.append(difere)
  for i in range(len(fileira)-1):
    print('"',format(float(fileira[i]),".2f"),'"', sep = "",end = ",")
  print('"',format(float(fileira[6]),".2f"),'"', sep = "")  