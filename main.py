def izdruka(daudzums, sar1):
  for elem in range(0,daudzums):
    print(sar1[elem])
  return 0

saraksts = [2,4,5,6,1,2,34,5]
daudzums = int(input("ievadi elementu skaistu: "))
rez = izdruka(daudzums, saraksts)